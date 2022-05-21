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
#### ```real_news.py```
- There is 3171 real news articles in the dataset.
- The output of this script is a .csv file named ```output_real.csv``` and a .png file named ```chart_real.png```. 
- The .csv file contains 6 columns named '*Text ID*', '*Title*', '*Negative*', '*Neutral*', '*Positive*' and '*Geopolitical Entities*'. 
- The .png file contains a bar chart with the top 20 GPEs in real news.  
   - The most frequent GPE is **US with 114** mentionings in the titles.
   - However, the third most frequent GPE is **America with 55** mentionings in the titles. 
   - Since US and America is referring to the same country there **combined frequency is 169**. 
   - The second most frequent GPE is **Iran with 94** mentionings in the real news, which could be a sign of something happened in Iran during the period the news are from. 
 - Both files can be found in the ```output``` folder

#### ```fake_news.py```
- There is 3164 fake news articles in the dataset.
- The output of this script is a .csv file named ```output_fake.csv``` and a .png file named ```chart_fake.png```. 
- The .csv file contains 6 columns named '*Text ID*', '*Title*', '*Negative*', '*Neutral*', '*Positive*' and '*Geopolitical Entities*'. 
- The .png file contains a bar chart with the top 20 GPEs in fake news.  
   - It is really interessting that **US/America** also are in a first and third place in the fake news. They even has a higher frequency in the fake news that in the real news, with a **combined frequency of 284** in the fake news. 
   - The second most frequent GPE is **Russia with 115** mentionings in the fake news.
   - Another notable observation in the top 20 GPEs is that **HILLARY** is mentioned 8 times in the titles in the fake news. It is clearly a problem that 'HILLARY' is getting labelled as a GPE eventhough I have run the script on the biggest NER model from SpaCy. 
- Both files can be found in the ```output``` folder


### Further development 
