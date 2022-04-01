# In terminal: 
# cd cds-lang/portfolio/assignment3 
    ## Or change to the directory that fits your filepath
# python src/network_analysis.py -fn 1H4.csv 
    ## -fn if single file, -d if directory

# parser
import argparse

# system tools
import os

# data analysis
import pandas as pd

# network analysis tools
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)

# get data for single file
def read_df(filename):
    filepath = os.path.join("..", "..", "..", 
                            "CDS-LANG", 
                            "network_data", 
                            filename) # Change filepath to ("input", filename)
    
    # load the data
    data = pd.read_csv(filepath, sep = "\t")
    return data

# parser
def parse_args():
    # Intialise argeparse
    ap = argparse.ArgumentParser()
    # command line parameters
    ap.add_argument("-fn", "--filename", required=False, help = "The filename to print")
    ap.add_argument("-d", "--directory", required=False, help = "The directory to print")
    # parse arguments
    args = vars(ap.parse_args())
    # return list of arguments
    return args

# main function
def main():
    # get arguments
    args = parse_args()
    data = read_df(args["filename"])
    print(data)

# create network
    # create a graph object called G
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    # plot network
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    # save network image
    outpath_viz = os.path.join('output','network.png')
    plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")

# find degrees from G
    degrees = G.degree()
    # convert to dataframe
    degrees_df = pd.DataFrame(degrees, columns = ["Name", "Degree"])

# find betweenness centrality from G
    bc = nx.betweenness_centrality(G)
    # convert to dataframa
    bc_df = pd.DataFrame(bc.items(), columns = ["Name", "Centrality"])

# find eigenvector_centrality from G
    ev = nx.eigenvector_centrality(G)
    # convert to dataframe 
    ev_df = pd.DataFrame(ev.items(), columns = ["Name", "Eigenvector"]).sort_values('Name', ascending=True)

# create list 
    list_data = list(zip(ev_df["Name"], degrees_df["Degree"], bc_df["Centrality"], ev_df["Eigenvector"]))
    
# convert list to dataframe
    data_output = pd.DataFrame(list_data, columns = ["Name", "Degree", "Betweenness centrality", "Eigenvector centrality"]) 

# display new dataframe
    print(data_output)
    
# save as csv
    csv = data_output.to_csv(os.path.join('output/network.csv'), encoding = "utf-8")
    return data_output
        
# python program to execute
if __name__ == "__main__":
    main()
    
    
    
    
# All of the above works for a single file, I've tried to get it to work on the whole directory and the below is want I wanted to do, but I couldn't manage to get it to work 


#def load_direc(directory):
    #filepath = os.path.join("..", "..", "..", 
                            #"CDS-LANG", 
                            #directory) # Change filepath to ("input", directory)
    #file_list = os.listdir(filepath)
    #return filepath, file_list
    
#def main():
    #if parse_args["filename"] is not None and parse_args["filename"].endswith(".csv"):
        #filepath = load_direc(args["filename"])
        #data = data_output(path)
        #outpath_viz(data, args["filename"])
        #csv(data, args["filename"]

    #elif parse_args["directory"] is not None:
        #results = load_direc(args["filename"])
        #for filename in results[1]:
            #if filename.endswith(".csv"):
                #filepath = f"{results[0]}/{filename}"
                #data = data_output(path)
                #outpath_viz(data, filename)
                #csv(data, filename)
            #else:
                #pass
    #else:
        #pass