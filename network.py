import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import math
from collections import Counter

df = pd.read_csv('csv/201505-citibike-tripdata.csv', header=0)

start_station_list = df['start station name'].tolist()
end_station_list = df['end station name'].tolist()

# Finding the nodes for network graph
print("Number of nodes in dataset: %d" % len(start_station_list))
print("Finding unique nodes...")
unique_nodes = list(set(start_station_list))
print("...done")
print("Number of unique nodes in dataset: %d" % len(unique_nodes))

# Calculating and concatenating edges between nodes
edgelist = list(zip(start_station_list, end_station_list))
unique_edges = list(set(edgelist))

# Verification
print("Number of edges in dataset: %d" % len(unique_edges))

edgecount = Counter(edgelist)

edge_weight = [[edge, edgecount[edge]] for edge in edgecount]
unique_edges = [[edge[0][0], edge[0][1], edge[1]] for edge in edge_weight]
#print(edge_weight)
#print(edge_weight[0])
#print(edge_weight[0][0])
#print(edge_weight[0][0][0])
#print(edge_weight[0][0][1])
#print(edge_weight[0][1])

# Creating the networkx graph
G = nx.MultiDiGraph()

#print(unique_nodes[0])
#print(unique_edges[0])
#for node in unique_nodes:
#    print(node)
#    G.add_node(node)

for edge in unique_edges:
    start_node = edge[0]
    end_node = edge[1]
    w = edge[2]
#    print(start_node, end_node, w)
    if w > 200:
        G.add_node(start_node)
        G.add_edge(start_node, end_node, weight=math.log10(w))


print(len(G))

plt.figure(1, figsize=(10,10))
nx.draw_networkx(G)
plt.axis('off')
plt.savefig("citibike_network_map.png")
