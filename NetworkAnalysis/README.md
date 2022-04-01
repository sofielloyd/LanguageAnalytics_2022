# Network Analysis - Assignment 3
This repository contains all of the code and data related to third assignment for my portfolio exam in the Spring 2022 module **Language Analytics** which is a part of my tilvalg in Cultural Data Science at Aarhus University.  

This repository is in active development, with new material being pushed on regularly from now and until **30th may 2022**.

## Assignment description 
Write a ```.py``` script that does the following: 
- If the user enters a *single filename* as an argument on the command line:
  - Load that edgelist
  - Perform network analysis using networkx
  - Save a simple visualisation
  - Save a CSV which shows the following for every node:
    - name; degree; betweenness centrality; eigenvector_centrality

- If the user enters a *directory name* as an argument on the command line:
  - Do all of the above steps for every edgelist in the directory
  - Save a separate visualisation and CSV for each file

## Goal
The goal of this assignment is to demonstrate that I have a good understanding of how to perform network analysis on undirected, weighted edgelists using networkx. 

## Technicalities 
The coding part of this repository will be run on Python. 

## Repo Structure  
This repository has the following directory structure:  

| **Folder** | **Description** |
| ----------- | ----------- |
| ```input``` | Input data |
| ```output``` | Output data |
| ```src``` | Python scripts |
