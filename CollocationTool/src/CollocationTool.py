# parser
import argparse

# import spacy package with english    
import spacy
nlp = spacy.load("en_core_web_sm")

# system tools
import os

# load math
import math

# data analysis
import pandas as pd

# regular expression
import re


# get data for single file
def read_file(filename):
    filepath = os.path.join("..",
                            "input",
                            filename)
    # load file
    with open(filepath, "r") as f:
        text = f.read()
    
    return text


# get data for file in folder
def read_folder(filename):
    filepath = os.path.join(filename)
    # load file
    with open(filepath, "r") as f:
        text = f.read()
        
    return text

        
# traverse through folder
def traverse(path):
    files_in_folder = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files_in_folder.append((file, path + "/" + str(file)))
    
    return files_in_folder


# parser
def parse_args():
    # intialise argeparse
    ap = argparse.ArgumentParser()
    # command line parameters
    ap.add_argument("-fn", "--filename", required=False, help = "The filename to print")
    ap.add_argument("-d", "--directory", required=False, help = "The directory to print")
    # parse arguments
    args = vars(ap.parse_args())
    
    # return list of arguments
    return args


# regex tokenizer for splitting files below
def tokenize(input_string):
    tokenizer = re.compile(r"\W+")
    
    return tokenizer.split(input_string)


# define Mutal Information function
def MI(A, B, AB, span, corpus_size):
    score = math.log((AB * corpus_size) / (A * B * span)) / math.log(2)
    
    return score


def collocation(text, filename = None):
    if filename is None:
        output_file = "collocates.csv"
    else:
        output_file = filename + "_collocates.csv"
    
    # define keyword
    keyword = "dog"
    # define window size
    window_size = 5
    
    # tokenize and cleanup the text
    tokenized_text = []

    for word in tokenize(text):
        # lowercase
        lowercase = word.lower()
        # cleanup punctuation etc
        cleaned = re.sub(r'[^\w\s]', '', lowercase)
        tokenized_text.append(cleaned)
        
    # create temporary list to get context word
    tmp = []
    # for the target word... 
    for idx,word in enumerate(tokenized_text):
        # if it's the keyword...
        if word == keyword:
            # left context catch start of list
            left_context = max(0, idx-window_size)
            right_context = idx+window_size
            # extract all words ± 5 and add to tmp list.
            full_context = tokenized_text[left_context:idx] + tokenized_text[idx+1:right_context]
            # append to list
            tmp.append(full_context)
            
    # flatten list
    flattened_list = []
    # for each sublist in list of lists
    for sublist in tmp:
        # for each item in sublist
        for item in sublist:
            # append
            flattened_list.append(item)

    # create a list of collocate counts
    collocate_counts = []

    # for every collocate 
    for word in set(flattened_list):
        # count how often each word appears as a collocate
        count = flattened_list.count(word)
        # append tuple of word and count to list
        collocate_counts.append((word, count))

    # define keyword frequence    
    keyword_freq = tokenized_text.count(keyword)
    # length of text
    corpus_size = len(tokenized_text)

    # create list for output parameters
    out_list = []
    # for every tuple in list of collocate count
    for tup in collocate_counts:
        coll_text = tup[0]
        coll_count = tup[1]
        total_occurrences = tokenized_text.count(coll_text)
        # calculate MI score
        score = MI(keyword_freq, coll_count, total_occurrences, 10, corpus_size)
        # append to out_list
        out_list.append((coll_text, coll_count, total_occurrences, score))

    # split out_list
    words = []
    colloc = []
    total = []
    score = []

    # for every tuple in out_list
    for a_tuple in out_list:
        words.append(a_tuple[0])
        colloc.append(a_tuple[1])
        total.append(a_tuple[2])
        score.append(a_tuple[3])

    # make list of content
    list_content = list(zip(words, 
                            colloc, 
                            total, 
                            score))

    # create dataframe
    data = pd.DataFrame(list_content, columns = ["context_word", 
                                                 "collocate_count", 
                                                 "total_count", 
                                                 "MI-score"]) 
    # print dataframe
    print(data)

    # save as csv
    csv = data.to_csv(os.path.join('../output/' + output_file), encoding = "utf-8")
    
    return data

    
def main():
    args = parse_args()
    if args["filename"] is not None:
        text = read_file(args["filename"])
        print(text)
        collocation(text)
        
    if args["directory"] is not None:
        files_in_folder = traverse(args["directory"])
        print(files_in_folder)
        for file in files_in_folder:
            text = read_folder(file[1])
            collocation(text, file[0])
    
    
# python program to execute
if __name__ == "__main__":
    main()
