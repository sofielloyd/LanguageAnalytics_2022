# Collocation Tool - Assignment 1
This repository contains all of the code and data related to first assignment for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  


## Assignment description 
Write a small Python program to perform collocational analysis using the string processing and NLP tools you've already encountered.   

My ```.py``` script does the following:  
- Take a user-defined search term and a user-defined window size.
- Take one specific text which the user can define.
- Find all the context words which appear ± the window size from the search term in that text.
- Calculate the mutual information score for each context word.
- Save the results as a CSV file with (at least) the following columns: 
  - the collocate term
  - how often it appears as a collocate
  - how often it appears in the text
  - the mutual information score.

### Goals and outcome of the assignment
- The goal of this assignment is to demonstrate that I have a good understanding of how to use simple text processing techniques to extract valuable information from text data.
- After completing this assignment, you will have a simple collocation tool which can in principal be resused on another text dataset of your choice.

## Methods
The coding part of this repository will be run in Python. 


## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the **100 english novels** which can be found **[here](inset link)**.  

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The ```collocation_tool.py``` can be run from the command line by changing the directory to ```src``` and then execute  ```python collocation_tool.py -fn *filename*``` for running the script on *a single file* or ```python collocation_tool.py -d *path to directory*``` for running the script on a *directory*.   
If you use the input folder, then the *path to directory* should be  ```../input```.

I have used the keyword, **dog**, but this can be changed in the script. 
 
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
#### For single file
- If the user runs the code for a single file, the output of this script will be a ```.csv``` file with all the context words to the keyword, how many times it appears as a collocate, how many times the context word appear in the text and the MI-score. 
- The filename for this output file is ```collocates.csv``` and can be found in the ```output``` folder. 

#### For directory
- If the user runs the code for the whole directory, the output of this script will be a ```.csv``` file for every text from the directory with all the context words to the keyword, how many times it appears as a collocate, how many times the context word appear in the text and the MI-score. 
  - The filenames for these output files is called ```*filename*_collocates.csv```.
  - These results will be saved to the ```output``` folder.  
  - If the keyword doesn't appear in the text, the .csv file will be empty.
- It should be noticed that I have selected a small amount of texts from the **100 english novels**, but the script would also work on the whole dataset. 

### Further development 
Some improvemnets for my code could be: 
- Add a parser which allows the user to define a number of different collocates at the same time, rather than only one.
- Add a parser which allows the user to define the keyword from the command line. 
- If the keyword doesn't occur in the text, leave the text out. 
