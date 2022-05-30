# Sentiment and Collocation on Religious Texts - Self-assigned project
This repository contains all of the code and data related to the self-assigned project for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  


## Assignment description 
My ```.py``` script does the following:
- Load the data.
- Make a sentiment analysis using ```Vader``` and ```TextBlob```.  
- Create a ```wordcloud``` to visualise most used words. 
- Take a user-defined search term based on the wordcloud, and a user-defined window size.
- Find all the context words which appear ± the window size from the search term in the text.
- Calculate the mutual information score for each context word. 
- Make a ```vader``` sentiment analysis on the context words. 
- Save results as a .csv file. 


### Goals and outcome of the assignment
- The goal of the project is to compare the Quran and the Bible in order to see if one of them is more positive than the other and which context words appears near the same keyword in both texts.  
- I also want to demonstrate my skills in Python related to language analytics, such as NLP.
- The code will provide a script which could be re-written and reused on separate data.


## Method
For this script I have first used ```vaderSentiment``` to make a sentiment analysis with the polarities *negative*, *neutral* and *positive*.  
I have then used ```spacytextblob```to make a sentiment analysis with *polarity* (negative = 0.0, positive = 1.0) and *subjectivity* (objective = -1.0), subjective = +1.0).  I have used ```statistics``` to calculate the mean score of the sentiment scores and ```matplotlib``` to visualise the *polarity* and *subjectivity* across the dataset.  
Further, I have used ```wordcloud``` to make a wordcloud of the most common words in the texts. I have used ```nltk.corpus```'s stopwords list to remove stopwords. I have used the wordcloud to find which words could be good to use for my collocation analysis. It turned out that *lord* is a very frequent word in both the quran and the bible, and that is why I have chosen *lord* to be the keyword for my collocation analysis.  
At last, I have used ```vaderSentiment``` to make a sentiment analysis on the collocate words in the texts and calculated how many of the collocate words are *negative*, *neutral* or *positive*.  



## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the english translation of the **Quran** by Yusuf Ali which can be found [here](https://www.kaggle.com/datasets/zusmani/the-holy-quran?select=en.yusufali.csv).  
I have also used the **King James Bible**, which has been provided by our instructor, Ross.  
I have renamed the datasets to **quran.csv** and **bible.csv** to get a neater look in the output files.  

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The scripts can be run from the command line by changing the directory to ```src``` and then execute  ```python sentiment_collocation.py -fn *filename*```.  


### Repo Structure  
This repository has the following directory structure:  

| **Folder** | **Description** | *Sub-folder* |
| ----------- | ----------- | ----------- |
| ```input``` | Input data |  |
| ```output``` | Output data | ```plots```, ```tables``` |
| ```src``` | Python scripts | |


- The ```input``` folders are empty and this is where you should upload your own data, if you want to reproduce the code.

- The ```output``` folders contains my results and it is this folder that you should save your own results when replicating the code. 
  - The sub-folder ```plots``` contains the plots of the networks in .png format.
  - The sub-folder ```tables``` contains .csv files with name, degree, betweenness centrality and eigenvector centrality

- The ```src``` folders contains the code written in ```.py``` scripts. 


## Discussion of results 
### Results 
#### Visualisations
- The visualisations are called ```*filename*_textblob.png``` and ```*filename*_wordcloud.png``` are saved in ```output/plots```.  
- The *_textblob.png* is a visualisation of the ```TextBlob``` sentiment analysis where the smoothed subjectivity and smoothed polarity is visualised. 
  - The *polarity* curve shows that the **Quran** is more negative towards the end, and also it seems as it becomes more objective at the end the text. 
  - Since the **Bible** isn't sorted (starting with genesis) it really doesn't say anything about whether the bible is most positive towards the end of it.    
- The *_wordcloud.png* is a visualisation of the ```wordcloud```. 
  - The most frequent words in the **Quran** is *allah* and *ye*. 
  - The most frequent words in the **Bible** is *lord*, *shall* and *god*. 

#### Tables
- The dataframes are called ```*filename*_sentiment.csv``` and ```*filename*_collocates.csv``` are saved in ```output/tables```. 
- The *_sentiment.csv* contains 6 columns named 'Text', 'Negative', 'Neutral', 'Positive', 'Subjectivity' and 'Polarity'. 
  - The mean of the scores for the **Quran** and the **Bible** are displayed below. 
 
- The *_collocates.csv* contains 7 columns named 'Context words', 'Collocate count', 'Total count',	'MI score',	'Negative',	'Neutral' and	'Positive'. 
  - I have removed the stopwords from the text to make it more clear which context words appears near the keyword (*lord*), because words like 'and', 'the' and 'of' isn't really interesting for analysis. 
  - I have sorted the dataframe by values in the column named 'Collocate count' in decending order, so that the context words that appears the most times near the keywords are at the top of the dataframe.  
  - The dataframe shows that *lord* often appears near *lord* which makes sense since *lord* is one of the most frequent words in both texts. 

#### Compare the Quran and the Bible
*These scores will also be displayed in the terminal when running the script*. 

| **Scores** | **Quran** | **Bible** | 
| ----------- | ----------- | ----------- |
| Negative sentiment | 0.086 | 0.063 |
| Neutral sentiment | 0.798 | 0.847 |
| Positive sentiment | 0.116 | 0.089 |
| Polarity score | 0.070 | 0.097 |
| Subjectivity score | 0.358 | 0.371 | 
| Frequency of keyword (lord) | 976 | 8749 |
| Total length of text | 896841 |  |
| Negative collocate words to keyword | 175 | 353 |
| Neutral collocate words to keyword | 1495 | 4325 |
| Positive collocate words to keyword | 231 | 343 |

### Further development 
Some improvements for this code could be: 
- Add an ```argparse``` argument which allows the user to define a number of different collocates at the same time, rather than only one.
- Add an ```argparse``` argument which allows the user to define the keyword from the command line.  
- Right now the script only works on .csv files where the third column contains the text. This of course gives some limmitation to the input file, and it would be a great improvement for the code to make it more reproducible by changing the code to be able to use all .csv files. 
- Remove stopwords from ```*filename*_collocates.csv```. 

