# Text Classification - Assignment 4
This repository contains all of the code and data related to fourth assignment for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  


## Assignment description 
We're going to be working with the data in the folder ```CDS-LANG/toxic``` and trying to see if we can predict whether or not a comment is a certain kind of *toxic speech*.  
Write two ```.py``` scripts which do the following:

- The first script should perform benchmark classification using standard machine learning approaches
  - This means ```CountVectorizer()``` or ```TfidfVectorizer()```, ```LogisticRegression``` classifier
  - Save the results from the classification report to a text file 
  
- The second script should perform classification using the kind of deep learning methods we saw in class
  - Keras ```Embedding``` layer, Convolutional Neural Network
  - Save the classification report to a text file 

### Goals and outcome of the assignment
- The goal of this assignment is to show that I can perform text classification using *both* classical machine learning approaches, as well as using more sophisticated deep learning approaches.
- The scripts can also be reused and modified for use on other text data in a tabular format.


## Method
### ```ML_classification.py```
For this script I have used ```CountVectorizer``` and ```LogisticRegression``` from the ```Scikit-learn``` package to perform standard machine learning. 

### ```DL_classification.py```
For this script I have used ```train_test_split``` from the ```Scikit-learn``` package to perform deep learning using a sequential model with an ```embedding``` layer from the ```Tensorflow``` package. 


## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the **Video Comments Threat Corpus** which can be found [here](https://www.simula.no/sites/default/files/publications/files/cbmi2019_youtube_threat_corpus.pdf).  

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The scripts can be run from the command line by changing the directory to ```src``` and then execute  ```python ML_classification.py``` *or* ```python DL_classification.py```.


### Repo Structure  
This repository has the following directory structure:  

| **Folder** | **Description** |
| ----------- | ----------- |
| ```input``` | Input data |
| ```output``` | Output data |
| ```src``` | Python scripts |
| ```utils``` | Additional Python functions |


- The ```input``` folders are empty and this is where you should upload your own data, if you want to reproduce the code.

- The ```output``` folders contains my results and it is this folder that you should save your own results when replicating the code. 

- The ```src``` folders contains the code written in ```.py``` scripts. 

- The ```utils``` folders contains a collection of small Python functions which make common patterns shorter and easier. The utils scripts used in this project were developed in-class and can also be found in [this](https://github.com/CDS-AU-DK/cds-language) repository.


## Discussion of results 
### Results 
#### ```ML_classification.py```
- The output of this script is the ```ML_report.txt``` which can be found in the output folder.
- The accuracy score is **0.79**.
- The precision score for the label *non-toxic* is **0.76**. 
- The precision score for the label *toxic* is **0.83**.


#### ```DL_classification.py```
- The output of this script is the ```DL_report.txt``` and ````confusion_matrix.csv``` which both can be found in the output folder.
- The classification report shows an accuracy score on **0.96**, a precision score for *non-toxic* on **0.97** and a precision score for *toxic* on **0.68**. 
- The confusion matix shows that **5389** of the non-toxic comments were predicted as being non-toxic, **64** of the non-toxic comments were predicted as being toxic, **139** of the toxic comments were predicted as being non-toxic, and **137** of the toxic comments were predicted as being toxic. 


### Further development 
Some improvements for this code could be: 
- To add a range of different ```Argparse``` parameters that would allow the user to interact with the code, such as the embedding dimension size and the CountVector parameters.

