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
The coding part of this repository will be run on Python. 

## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the **toxic dataset** which can be found [here](https://www.simula.no/sites/default/files/publications/files/cbmi2019_youtube_threat_corpus.pdf).  

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
- The accuracy score is **XX**
- The precision score is best for ```toxic``` and worst for ```non-toxic```.


#### ```DL_classification.py```
- The output of this script is the ```DL_report.txt``` which can be found in the output folder.
- The accuracy score is **XX**
- The precision score is best for ```non-toxic``` and worst for ```toxic```.

### Further development
