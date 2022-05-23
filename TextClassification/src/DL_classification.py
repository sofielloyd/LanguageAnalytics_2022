# path tools
import sys,os
sys.path.append(os.path.join(".."))

# simple text processing tools
import re
import tqdm
import unicodedata
import contractions
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')

# data wranling
import pandas as pd
import numpy as np

from utils import classifier_utils as clf

# tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, 
                                     Flatten,
                                     Conv1D, 
                                     MaxPooling1D, 
                                     Embedding)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.regularizers import L2

# scikit-learn
from sklearn.metrics import (confusion_matrix,
                             classification_report)
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

# visualisations 
import matplotlib.pyplot as plt

# fix random seed for reproducibility
seed = 42
np.random.seed(seed)


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    
    return stripped_text


def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    return text


def pre_process_corpus(docs):
    norm_docs = []
    for doc in tqdm.tqdm(docs):
        doc = strip_html_tags(doc)
        doc = doc.translate(doc.maketrans("\n\t\r", "   "))
        doc = doc.lower()
        doc = remove_accented_chars(doc)
        doc = contractions.fix(doc)
        # lower case and remove special characters\whitespaces
        doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
        doc = re.sub(' +', ' ', doc)
        doc = doc.strip()  
        norm_docs.append(doc)
  
    return norm_docs


# get data
def load_data():
    # filepath
    filename = os.path.join("..", "input", "VideoCommentsThreatCorpus.csv")

    # load dataframe
    data = pd.read_csv(filename)

    # rename variables
    labels = data["label"].replace({0:"non-toxic", 1:"toxic"}, inplace=True)

    # create new variables
    X = data["text"]
    y = data["label"]

    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = 0.2,
                                                        random_state = 42)

    # normalize
    X_train_norm = pre_process_corpus(X_train)
    X_test_norm = pre_process_corpus(X_test)
    
    # create one-hot encodings 
    lb = LabelBinarizer()
    y_train_lb = lb.fit_transform(y_train)
    y_test_lb = lb.fit_transform(y_test)
    
    return y_test, X_train_norm, y_train_lb, X_test_norm, y_test_lb, labels


# function for tokenization of sequences
def sequences(X_train_norm, X_test_norm):
    # define out-of-vocabulary token
    t = Tokenizer(oov_token = '<UNK>')

    # fit the tokenizer on then documents
    t.fit_on_texts(X_train_norm)

    # set padding value
    t.word_index["<PAD>"] = 0 

    # tokenize sequences
    X_train_seqs = t.texts_to_sequences(X_train_norm)
    X_test_seqs = t.texts_to_sequences(X_test_norm)

    print(f"Vocabulary size={len(t.word_index)}")
    print(f"Number of Documents={t.document_count}")
    
    # define max sequence length
    MAX_SEQUENCE_LENGTH = 1000

    # add padding to sequences
    X_train_pad = sequence.pad_sequences(X_train_seqs, maxlen=MAX_SEQUENCE_LENGTH, padding="post")
    X_test_pad = sequence.pad_sequences(X_test_seqs, maxlen=MAX_SEQUENCE_LENGTH, padding="post")
    
    return X_train_pad, X_test_pad, t
    

# create model for training 
def create_model(t):
    # overall vocublarly size
    VOCAB_SIZE = len(t.word_index)
    # number of dimensions for embeddings
    EMBED_SIZE = 300

    # create the model
    model = Sequential()
    # embedding layer
    model.add(Embedding(VOCAB_SIZE, 
                        EMBED_SIZE, 
                        input_length=1000))

    # first convolution layer and pooling
    model.add(Conv1D(filters=128,
                     kernel_size=4,
                     padding='same',
                     activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # second convolution layer and pooling
    model.add(Conv1D(filters=64, 
                     kernel_size=4, 
                     padding='same',
                     activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # third convolution layer and pooling
    model.add(Conv1D(filters=32, 
                     kernel_size=4,
                     padding='same',
                     activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # fully-connected classification layer
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    
    # compile model
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    # print model summary
    model.summary()
    
    return model
    
    
# evaluate model 
def evaluate(model, X_test_pad, y_test_lb, labels, y_test):
    
    # final evaluation of the model
    scores = model.evaluate(X_test_pad, y_test_lb, verbose=1)
    print(f"Accuracy: {scores[1]}")

    # predict model
    predictions = (model.predict(X_test_pad) > 0.5).astype("int32")
    # assign labels
    predictions = ['toxic' if item == 1 else 'non-toxic' for item in predictions]
    
    # create classification report
    report = classification_report(y_test, predictions)
    
    print(report)

    # save the classification report 
    with open('../output/DL_report.txt', 'w') as file:
        file.write(report)
    
    # set labels for confusion matrix
    labels = ['non-toxic', 'toxic']
    # create confusion matric
    df = pd.DataFrame(confusion_matrix(y_test, predictions), 
                      index=labels, 
                      columns=labels)
    
    # save confusion matrix to .csv file
    df.to_csv("../output/confusion_matrix.csv", encoding = "utf-8")

    
def main():
    # clear session
    tf.keras.backend.clear_session 
    
    # get data
    y_test, X_train_norm, y_train_lb, X_test_norm, y_test_lb, labels = load_data()
    
    # tokenize sequences
    X_train_pad, X_test_pad, t = sequences(X_train_norm, X_test_norm)
    
    # build model
    model = create_model(t)
    
    # train model
    model.fit(X_train_pad, 
              y_train_lb,
              epochs = 10,
              batch_size = 128,
              validation_split = 0.2,
              verbose = True)
    
    # evaluate model 
    evaluate(model, 
             X_test_pad, 
             y_test_lb, 
             labels, 
             y_test)

    
# python program to execute
if __name__ == "__main__":
    main()