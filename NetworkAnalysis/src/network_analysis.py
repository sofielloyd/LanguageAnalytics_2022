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
    filepath = os.path.join("..", 
                            "input",
                            filename)
    
    # load the data
    data = pd.read_csv(filepath, sep = "\t")
    
    return data


# get data for file in folder
def read_file(filename):
    filepath = os.path.join(filename)
    
    # load the data
    data = pd.read_csv(filepath, sep = "\t")
    
    return data


# traverse through folder
def traverse(path):
    files_in_folder = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files_in_folder.append((file, path + "/" + str(file)))
    
    return files_in_folder


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
        
    
# function for network analysis        
def analysis(data, filename = None):
    if filename is None:
        output_image = "single_network.png"
        output_file = "single_network.csv"
    else:
        output_image = filename + "_network.png"
        output_file = filename + "_network.csv"
        
    # create a graph object called G
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    # plot network
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    # save network image
    outpath_viz = os.path.join('..', 'output', output_image)
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
    csv = data_output.to_csv(os.path.join('../output/' + output_file), encoding = "utf-8")
    
    return data_output


# main function
def main():
    args = parse_args()
    if args["filename"] is not None:
        data = read_df(args["filename"])
        print(data)
        analysis(data)
    
    if args["directory"] is not None:
        files_in_folder = traverse(args["directory"])
        print(files_in_folder)
        for file in files_in_folder:
            data = read_file(file[1])
            analysis(data, file[0])
            
        
# python program to execute
if __name__ == "__main__":
    main()