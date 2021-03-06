# Network Analysis - Assignment 3
This repository contains all of the code and data related to third assignment for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  


## Contribution 
This assignment was conduted in collaboration with Laura Louise Rokkjær (student no.: 201908876) and some of the code may be equivalent to each other. 


## Assignment description 
Write a ```.py``` script that does the following: 
- If the user enters a *single filename* as an argument on the command line:
  - Load that edgelist
  - Perform network analysis using ```networkx```
  - Save a simple visualisation
  - Save a CSV which shows the following for every node:
    - name
    - degree
    - betweenness centrality
    - eigenvector_centrality

- If the user enters a *directory name* as an argument on the command line:
  - Do all of the above steps for every edgelist in the directory
  - Save a separate visualisation and CSV for each file


### Goals and outcome of the assignment
- The goal of this assignment is to demonstrate that I have a good understanding of how to perform network analysis on undirected, weighted edgelists using ```networkx```. 
- This script can be resued for future projects to perform a quick, simple network analysis.

## Method
First I create a graph (G) using ```networkx``` and then uses ```draw_networkx``` to create a network from the graph.  
Furthermore, I uses ```networkx``` to find the ```degree()```, ```betweenness_centrality()``` and ```eigenvector_centrality()```.  
Using ```pandas``` I append these values into a dataframe.  
I have also added two ```argparse``` arguments, so the user can enter either a single filename or a directory on the command line.   

## Usage
In order to reproduce this code, you'll need to uploade your own data into the ```input``` folder.   
I have used the **network data** which has been provided by our instructor, Ross.     

You'll also have to install the needed packages, which can be found in ```requirements.txt```. 

The ```network_analysis.py``` can be run from the command line by changing the directory to ```src``` and then execute  ```python network_analysis.py -fn *filename*``` for running the script on *a single file* or ```python network_analysis.py -d *path to directory*``` for running the script on a directory.   
If you use the input folder, then the *path to directory* should be  ```../input```.

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
#### For single file
- If the user runs the code for a single file, the output of this script will be a ```.csv``` file with the Named Entity, degree, betweenness centrality and eigenvector centrality. Their will also be created a ```.png``` file which contains a visualisation of the network.
  - The visualisation are called ```single_network.png``` and are saved in ```output/plots```.  
  - The dataframe are called ```single_network.csv``` and are saved in ```output/tables```. 


#### For directory
- If the user runs the code for the whole directory, the output of this script will be a ```.csv``` file for every file in the directory with the Named Entity, degree, betweenness centrality and eigenvector centrality. Their will also be created a ```.png``` file for every file in the directory which contains a visualisation of the network.
  - The visualisations are called ```*filename*_network.png``` and are saved in ```output/plots```.  
  - The dataframes are called ```*filename*_network.csv``` and are saved in ```output/tables```. 
   
### Further development 
An improvement for the code could be:
- Allow the user to choose between the different plotting algorithms that offers ```networkx```.
