# pip install networkx pandas
# 
import networkx as nx
import pandas as pd
from collections import defaultdict

def calculate_pagerank(file_path):
    # Read the edgelist from the file
    G = nx.read_edgelist(file_path, create_using=nx.DiGraph(), nodetype=int)
    
    # Calculate PageRank scores
    pagerank = nx.pagerank(G)
    
    # Get the top 10 pages based on PageRank scores
    top_pages = sorted(pagerank, key=pagerank.get, reverse=True)[:10]
    
    # Create a dictionary to store results
    results = defaultdict(float)
    
    # Populate the dictionary with top pages and their PageRank scores
    for page in top_pages:
        results[page] = pagerank[page]
    
    return results

# Specify the file path (replace this with your file path)
file_path = 'path/to/your/edgelist/file.txt'

# Calculate PageRank and get the top pages with their ranks
top_pages_with_ranks = calculate_pagerank(file_path)

# Display the results
print("Top Pages with PageRank Scores:")
for page, rank in top_pages_with_ranks.items():
    print(f"Page {page}: PageRank {rank}")
