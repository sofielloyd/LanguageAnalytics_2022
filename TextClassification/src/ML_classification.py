# path tools
import sys,os
sys.path.append(os.path.join(".."))

# data munging tools
import pandas as pd
from utils import classifier_utils as clf

# tools from sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


# get data
def load_data():
    # get data
    filename = os.path.join("..", "input", "VideoCommentsThreatCorpus.csv")

    # load dataframe
    data = pd.read_csv(filename)
    
    # rename variables
    data["label"].replace({0:"non-toxic", 1:"toxic"}, inplace=True)
    
    # balance data
    data_balanced = clf.balance(data, 1000)
    
    # create new variables
    X = data_balanced["text"]
    y = data_balanced["label"]
    
    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = 0.2,
                                                        random_state = 42)
    
    return X_train, X_test, y_train, y_test


# logistic regression classification 
def logistic_regression(X_train, X_test, y_train, y_test):
    # create vectorizer object
    vectorizer = CountVectorizer(ngram_range = (1,2),
                                 lowercase = True,      
                                 max_df = 0.95,           
                                 min_df = 0.05,          
                                 max_features = 500)  
    
    # fit to the training data
    X_train_feats = vectorizer.fit_transform(X_train)

    # fit to the test data
    X_test_feats = vectorizer.transform(X_test)

    # get feature names
    feature_names = vectorizer.get_feature_names()

    # create classifier object
    classifier = LogisticRegression(random_state = 42).fit(X_train_feats, y_train)

    # make predictions
    y_pred = classifier.predict(X_test_feats)
    
    # Print the classification report to the terminal
    report = classification_report(y_test, y_pred)
    print(report)

    # Save the classification report 
    with open('../output/ML_report.txt', 'a') as my_txt_file:
        my_txt_file.write(report)
        

def main():
    # get data
    X_train, X_test, y_train, y_test = load_data()
    # logistic regression classification 
    logistic_regression(X_train, X_test, y_train, y_test)
    
    
# python program to execute
if __name__ == "__main__":
    main()