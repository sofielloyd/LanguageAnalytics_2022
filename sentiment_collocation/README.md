# Sentiment and Collocation on religious texts - Self-assigned project
This repository contains all of the code and data related to the self-assigned project for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  


## Assignment description 


### Goals and outcome of the assignment


## Method



## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the english translation of the **Quran** by Yusuf Ali which can be found [here](https://www.kaggle.com/datasets/zusmani/the-holy-quran?select=en.yusufali.csv).  
I have also used the **King James Bible**, which has been provided by our instructor, Ross.  
I have renamed the datasets to **quran.csv** and **bible.csv** to get a neater look in the output.  

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The scripts can be run from the command line by changing the directory to ```src``` and then execute  ```python sentiment_collocation.py -fn *filename*```.  


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


### Further development 
Some improvements for this code could be: 
- Add an ```argparse``` argument which allows the user to define a number of different collocates at the same time, rather than only one.
- Add an ```argparse``` argument which allows the user to define the keyword from the command line.  

