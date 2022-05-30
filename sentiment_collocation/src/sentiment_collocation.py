# system tools
import os
import argparse

# import spacy package with english    
import spacy
nlp = spacy.load("en_core_web_lg")

# load math
import math

# importing the statistics module
import statistics

# visualisations
import matplotlib.pyplot as plt

# data analysis
import pandas as pd
import numpy as np
from collections import Counter
from wordcloud import WordCloud
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# sentiment analysis VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# sentiment analysis TextBlob
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob
nlp.add_pipe('spacytextblob')


# load data 
def read_data(filename):
    filepath = os.path.join("../input", filename)
    # load the data
    df = pd.read_csv(filepath)
    # rename columns
    df.rename(columns={ df.columns[2]: "text" }, inplace = True)
    # make text lower case and convert to string
    df['text'] = df['text'].str.lower()
    
    # convert text column in dataframe to txt file 
    with open("../input/text.txt", 'w') as f:
        txt_file = df["text"]
        for text in txt_file:
            f.write(text)
    
    # read new text file
    filename = os.path.join("../input/text.txt")
    # open file
    with open(filename, "r") as f:
        text = f.read()
        
    return df, text


# add parser 
def parse_args():
    # intialise argeparse (ap)
    ap = argparse.ArgumentParser()
    # command line parameters
    ap.add_argument("-fn", "--filename", required=False, help = "The filename to print")
    # parse arguments
    args = vars(ap.parse_args())
   
    return args    


# sentiment analysis using vader
def vader(df):
    # create empty list
    vader_scores = [] 

    # for every headline in the fake news df using the column named "title"
    for headline in df["text"]: 
        # get the polarity score of the headline
        score = analyzer.polarity_scores(headline) 
        # append score to empty list
        vader_scores.append(score) 
        
    # convert to dataframe
    vader_df = pd.DataFrame(vader_scores)
    
    print(vader_df)
    
    # calculate mean score of negative sentiment
    mean_neg = statistics.mean(vader_df["neg"])
    print(f"Mean of negative sentiment in the text is {mean_neg}")
    
    # calculate mean score of neutral sentiment
    mean_neu = statistics.mean(vader_df["neu"])
    print(f"Mean of neutral sentiment in the text is {mean_neu}")
    
    # calculate mean score of positive sentiment
    mean_pos = statistics.mean(vader_df["pos"])
    print(f"Mean of positive sentiment in the text is {mean_pos}")
    
    return vader_df


# sentiment analysis using TextBlob
def text_blob(df, vader_df, filename):
    
    # get polarity scores for all words
    polarity = []
    for word in df["text"]:
        doc = nlp(word)
        score = doc._.blob.polarity
        polarity.append(score)
    
    # calculate mean score of polarity
    mean_polarity = statistics.mean(polarity)
    print(f"Mean of polarity score is {mean_polarity}")
    
    # get subjectivity scores for all words
    subjectivity = []
    for word in df["text"]:
        doc = nlp(word)
        score = doc._.blob.subjectivity   
        subjectivity.append(score)

    # calculate mean score of subjectivity       
    mean_subjectivity = statistics.mean(subjectivity)
    print(f"Mean of subjectivity score is: {mean_subjectivity}")
    
    # smoothen polarity
    smoothed_polarity = pd.Series(polarity).rolling(500).mean()
    
    # smoothen subjectivity
    smoothed_subjectivity = pd.Series(subjectivity).rolling(500).mean()

    # initialise the subplot function using number of rows and columns
    fig, ax = plt.subplots(2,1)
    # set title
    fig.suptitle('Smoothed TextBlob scores')

    # plot smoothed polarity
    ax[0].plot(smoothed_polarity)
    # add axes labels
    ax[0].set_ylabel("Polarity")

    # plot smoothed subjectivity
    ax[1].plot(smoothed_subjectivity)
    # add axes labels
    ax[1].set_xlabel("Number of rows in dataframe")
    ax[1].set_ylabel("Subjectivity")

    # save plot as png
    fig.savefig(os.path.join("../output/plots/" + filename + "_textblob.png"), bbox_inches="tight")
    
    # create list with sentiment scores
    list_sentiment = list(zip(df["text"],
                              vader_df["neg"], 
                              vader_df["neu"],
                              vader_df["pos"],
                              subjectivity, 
                              polarity))

    # convert to dataframe and name columns
    sentiment_df = pd.DataFrame(list_sentiment, columns = ["Text", 
                                                           "Negative", 
                                                           "Neutral", 
                                                           "Positive", 
                                                           "Subjectivity", 
                                                           "Polarity"]) 
    
    # convert to csv file and save
    sentiment_df.to_csv(os.path.join("../output/tables/" + filename + "_sentiment.csv"), encoding = "utf-8")
   
    return sentiment_df
 

# wordcloud
def wordcloud(df, filename):
    # define stopwords
    stop_words = set(stopwords.words('english'))
    comment_words = ''
    
    # iterate through the text in the csv file
    for val in df.text:
        # typecaste each val to string
        val = str(val)
        # split the value
        tokens = val.split()
        comment_words += " ".join(tokens)+" "

    # create wordcloud
    wordcloud = WordCloud(width = 800, 
                          height = 800,
                          background_color ='white',
                          stopwords = stop_words,
                          min_font_size = 10).generate(comment_words)

    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    # save plot
    plt.savefig(os.path.join("../output/plots/" + filename + "_wordcloud.png"), bbox_inches="tight")

    return wordcloud, stop_words


# function to remove puncation
def remove_punc(string):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:  
        if ele in punc:  
            string = string.replace(ele, " ") 
    
    return string
    
    
# function to calculate MI score
def MI(A, B, AB, span, corpus_size):
    score = math.log((AB * corpus_size) / (A * B * span)) / math.log(2)
    
    return score


# collocation tool
def collocation(text, stop_words, filename):
        
    # clean text for punctations
    clean = remove_punc(text)
    
    # remove stop words
    word_tokens = word_tokenize(clean)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    
    # define keyword
    key = "lord"
    
    # define window size
    window_size = 5
    
    # define counter
    counter = 0

    # make a for loop for counter
    for token in filtered_sentence:
        if token == key:
            counter = counter + 1 # for every 'key' go 1 counter up.
        else:
            pass

    # print
    print(f"'{key}' is mentioned {counter} in the text")
    
    # create temporary list
    tmp = []
    # for the target word... 
    for idx,word in enumerate(filtered_sentence):
        # if it's the keyword...
        if word == key:
            # left context catch start of list
            left_context = max(0, idx-window_size)
            right_context = idx+window_size
            # ... extract all words ± 5 and add to tmp list.
            full_context = filtered_sentence[left_context:idx] + filtered_sentence[idx+1:right_context]
            # append to list
            tmp.append(full_context)
    
    # flatten list
    flattened_list = []
    # for each sublist in list of lists
    for sublist in tmp:
        # ...and for each item in sublist
        for item in sublist:
            # append to list
            flattened_list.append(item)
    
    # create a list of collocate counts
    collocate_counts = []
    # for every collocate 
    for word in set(flattened_list):
        # count how often each word appears as a collocate
        count = flattened_list.count(word)
        # append tuple of word and count to list
        collocate_counts.append((word, count))
    
    # define keyword frequency
    keyword_freq = filtered_sentence.count(key)
    # corpus size
    corpus_size = len(filtered_sentence)
    
    # create list for output parameters
    out_list = []
    # for every tuple in list of collocate count
    for tup in collocate_counts:
        # find very collocate
        coll_text = tup[0] 
        # find collocate count
        coll_count = tup[1]
        # find total count of collocate in text
        total_occurrences = filtered_sentence.count(coll_text)
        # calculate MI score
        score = MI(keyword_freq, coll_count, total_occurrences, 10, corpus_size)
        # append to list
        out_list.append((coll_text, coll_count, total_occurrences, score))
        
    # convert to dataframe
    colloc_data = pd.DataFrame(out_list)  
                              
    # create empty list
    collocation_sentiment = [] 

    # for every word in the dataframe use the first column 
    for word in colloc_data[0]: 
        # get the polarity score of the words
        score = analyzer.polarity_scores(word) 
        # append score to list
        collocation_sentiment.append(score)
     
    # convert to dataframe
    collocation_df = pd.DataFrame(collocation_sentiment)
    
    # make list of content
    list_content = list(zip(colloc_data[0], 
                            colloc_data[1],
                            colloc_data[2],
                            colloc_data[3],
                            collocation_df["neg"],
                            collocation_df["neu"],
                            collocation_df["pos"]))
    
    # create dataframe and name columns
    collocation_df = pd.DataFrame(list_content, columns = ["Context words", 
                                                           "Collocate count", 
                                                           "Total count", 
                                                           "MI score", 
                                                           "Negative", 
                                                           "Neutral",
                                                           "Positive"])
    
    # sort values by column named 'Collocate count' in decending order
    collocation_df = collocation_df.sort_values(by="Collocate count",  ascending=False)
    
    # convert to csv and save
    collocation_df.to_csv(os.path.join("../output/tables/" + filename + "_collocates.csv"), encoding = "utf-8")
    
    # print dataframe
    print(collocation_df)
    
    # calculate number of negative collocate words to the keyword
    count_neg = collocation_df["Negative"].value_counts()
    print(f"There is {count_neg[1]} negative collocate words to '{key}'.")
  
    # calculate number of neutral collocate words to the keyword
    count_neu = collocation_df["Neutral"].value_counts()
    print(f"There is {count_neu[1]} neutral collocate words to '{key}'.")
    
    # calculate number of positive collocate words to the keyword
    count_pos = collocation_df["Positive"].value_counts()
    print(f"There is {count_pos[1]} positive collocate words to '{key}'.")
    
    return collocation_df


def main():
    args = parse_args()
    df, text = read_data(args["filename"])
    # vader sentiment analysis
    vader_df = vader(df)
    # textblob sentiment analysis
    text_blob(df, vader_df, args["filename"])
    # wordcloud
    stop_words = wordcloud(df, args["filename"])
    # collocation 
    collocation(text, stop_words, args["filename"])
    
    
# python program to execute
if __name__ == "__main__":
    main()