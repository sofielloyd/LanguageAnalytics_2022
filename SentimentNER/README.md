# Sentiment and NER - Assignment 2
This repository contains all of the code and data related to the second assignment for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  

## Assignment description 
Write a small Python program to perform NER and sentiment analysis. 
You have the choice of one of two different tasks:

1. Using the corpus of English novels, write some code which does the following tasks

   - For every novel in the corpus
     - Get the sentiment of the final sentence.
     - Plot the results over time, with one visualisation showing sentiment of opening sentences over time and one of closing sentences over time.
     - Find the 20 most common geopolitical entities mentioned across the whole corpus - plot the result as a bar chart.

**OR**

2. Using the corpus of Fake vs Real news, write some code which does the following

   - Split the data into two datasets - one of Fake news and one of Real news
   - For every headline
     - Get the sentiment scores
     - Find all mentions of geopolitical entites
     - Save a CSV which shows the text ID, the sentiment scores, and column showing all GPEs in that text
   - Find the 20 most common geopolitical entities mentioned across each dataset 
      - plot the results as a bar charts
  


### Goals and outcome of the assignment
- The goal of this assignment is to demonstrate that I have a good understanding of how to perform dictionary-based sentiment analysis.
- It also demonstrates that I can use off-the-shelf NLP frameworks like ```spaCy``` to perform named entity recognition and extraction.
- After completing this assignment, I will have the core skills required to perform similar analysis of other text corpora more relevant to your interests.


## Method 

## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the **Fake vs Real News** which can be found **[here](inset link)**.  

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The ```sentiment_ner.py``` can be run from the command line by changing the directory to ```src``` and then execute  ```python sentiment_ner.py``` 


### Repo Structure  
This repository has the following directory structure:  

| **Folder** | **Description** |
| ----------- | ----------- |
| ```input``` | Input data |
| ```output``` | Output data |
| ```src``` | Python scripts |


- The ```input``` folders are empty and this is where you should upload your own data, if you want to reproduce the code.

- The ```output``` folders contains my results and it is this folder that you should save your own results when replicating the code. 

- The ```src``` folders contains the code written in ```.py``` scripts. 


## Discussion of results 
### Results
The results of the script is two .csv files, named ```output_real.csv``` and ```output_fake.csv```, and two .png files, named ```chart_real.png``` and ```chart_fake.png```.   
The .csv files contains 6 columns named '*Text ID*', '*Title*', '*Negative*', '*Neutral*', '*Positive*' and '*Geopolitical Entities*'.   
The .png files contains a bar chart with the top 20 GPEs in fake news and real news.   
All these results can be found in the ```output``` folder. 


### Further development 
