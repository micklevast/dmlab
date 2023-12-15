import networkx as nx
import pandas as pd

def calculate_hits(graph):
    hits_scores = nx.hits(graph)
    authority_scores = hits_scores[1]
    hub_scores = hits_scores[0]
    
    return authority_scores, hub_scores

# Example Usage
# Create a directed graph (replace this with your graph data)
graph = nx.DiGraph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1), (3, 4), (4, 2)])

# Calculate HITS scores
authority_scores, hub_scores = calculate_hits(graph)

# Display the results
authority_results = pd.DataFrame(list(authority_scores.items()), columns=['Page', 'AuthorityScore'])
hub_results = pd.DataFrame(list(hub_scores.items()), columns=['Page', 'HubScore'])

print("Authority Scores:")
print(authority_results)

print("\nHub Scores:")
print(hub_results)
