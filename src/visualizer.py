# import networkx as nx
# import matplotlib.pyplot as plt

# # Create a graph
# G = nx.Graph()

# # Add nodes with labels
# G.add_node(1, label='ITB')
# G.add_node(2, label='')
# G.add_node(3, label='C')
# G.add_node(4, label='D')

# # Add edges with weights
# G.add_edge(1, 2, weight=0.5)
# G.add_edge(2, 3, weight=1.0)
# G.add_edge(3, 4, weight=1.5)
# G.add_edge(4, 1, weight=2.0)

# # Set positions for nodes (optional)
# pos = nx.spring_layout(G)

# # Draw nodes with labels
# nx.draw_networkx_nodes(G, pos, node_size=500)
# nx.draw_networkx_labels(G, pos, labels={n: G.nodes[n]['label'] for n in G.nodes()}, font_size=16)

# # Draw edges with weights
# edge_labels = {(u, v): f"{G[u][v]['weight']}" for (u, v) in G.edges()}
# nx.draw_networkx_edges(G, pos, width=2)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# # Display the graph
# plt.axis('off')
# plt.show()

import networkx as nx
from graph import *
import matplotlib.pyplot as plt

# create a graph
G = LocationGraph()

# add some nodes and edges
# G.add_weighted_edges_from([(1,2,3), (2,3,3), (3,4,1), (4,5,3), (5,6,5), (6,7,8), (7,8,6), (8,9,7)])
G.add_weighted_edges_from("ITB", 2, 3)
G.add_weighted_edges_from(2, 3, 3)
G.add_weighted_edges_from(3,4,1)
G.add_weighted_edges_from(4,5,3)
G.add_weighted_edges_from(5,6,5)
G.add_weighted_edges_from(6,7,8)
G.add_weighted_edges_from(7,8,6)
G.add_weighted_edges_from(5,"mcd",20)
G.add_weighted_edges_from(8,"mcd",7)

for nei in G.neighbors(3): 
    print(nei) 

# define the path to color
path = [1, 2, 3, 4, 5]

# create a list of edge colors
edge_colors = []
for edge in G.edges():
    if edge[0] in path and edge[1] in path:
        edge_colors.append('r')
    else:
        edge_colors.append('k')

# draw the graph with the colored path
pos = nx.spring_layout(G)
nx.draw(G, pos, edge_color=edge_colors, with_labels=True)

# Draw edges with weights
edge_labels = {(u, v): f"{G[u][v]['weight']}" for (u, v) in G.edges()}
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.show()