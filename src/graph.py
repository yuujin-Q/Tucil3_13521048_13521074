"""
:file: graph.py

a wrapper class for nx.DiGraph (NetworkX's Directed Graph)
"""

import networkx as nx
import matplotlib.pyplot as plt
from utils import *


class LocationGraph(nx.DiGraph):
    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)

    def add_node(self, node_name, latitude=0, longitude=0):
        """add new node, overrides method from nx.DiGraph

        :param node_name:
        :param latitude:
        :param longitude:
        """
        super().add_node(node_name, lat=latitude, lon=longitude)

    def add_weighted_edge(self, start_node_name, finish_node_name, weight):
        """add weighted edge using add_weighted_edges_from method

        :param start_node_name:
        :param finish_node_name:
        :param weight:
        :return:
        """
        return super().add_weighted_edges_from([(start_node_name, finish_node_name, weight)])

    def get_neighbors(self, n):
        """get iterator of neighbor of node_name n

        :param n: node name
        :return: iterator to neighbors of n
        """
        # return iterator to neighbors of n
        return super().neighbors(n)

    def get_edge_cost(self, start_node_name, finish_node_name):
        """get edge cost of an edge, might be 'inf'

        :param start_node_name:
        :param finish_node_name:
        :return: cost of directed edge
        """
        cost = self.get_edge_data(start_node_name, finish_node_name)
        if cost is None:
            return float('inf')
        else:
            return cost['weight']

    def get_distance_between(self, start_node_name, finish_node_name):
        """haversine distance between two nodes, used in astar heuristic

        :param start_node_name:
        :param finish_node_name:
        :return: haversine distance
        """
        # check for invalid node parameter
        if (not self.has_node(start_node_name)) or (not self.has_node(finish_node_name)):
            return float('inf')
        else:
            # haversine distance
            node_1 = self.nodes[start_node_name]
            node_2 = self.nodes[finish_node_name]

            return haversine_distance(node_1['lat'], node_1['lon'], node_2['lat'], node_2['lon'])

    def display_graph(self, with_weights=True, solution_path=[]):
        """display graph using nx.draw and matplotlib.pyplot

        :param with_weights:
        :param solution_path:
        """
        node_pos = {n: (d['lon'], d['lat']) for n, d in self.nodes(data=True)}
        node_index = {n: (idx + 1) for idx, n in enumerate(self.nodes())}

        if solution_path:
            # create a list of edge colors
            edge_colors = []
            edge_route_tuples = [(solution_path[i], solution_path[i + 1]) for i in range(len(solution_path) - 1)]

            for edge in self.edges():
                if edge in edge_route_tuples:
                    edge_colors.append('y')
                else:
                    edge_colors.append((0.5, 0.5, 0.5, 0.5))  # transparent gray

            # create a list of node colors
            node_colors = []
            for node in self.nodes():
                if node == solution_path[0]:
                    node_colors.append('g')
                elif node == solution_path[len(solution_path) - 1]:
                    node_colors.append('r')
                elif node in solution_path:
                    node_colors.append('y')
                else:
                    node_colors.append('c')

        else:
            edge_colors = (0.5, 0.5, 0.5, 0.5)  # default: transparent gray, cyan
            node_colors = 'c'

        # Draw nodes, node indices, edges, solution edges
        nx.draw(self, pos=node_pos, labels=node_index, edge_color=edge_colors, node_color=node_colors)

        if with_weights is True:
            # Draw edges with weights
            edge_labels = {(u, v): f"{self[u][v]['weight'] : .2f}" for (u, v) in self.edges()}
            nx.draw_networkx_edge_labels(self, node_pos, edge_labels=edge_labels, label_pos=0.7)

        plt.axis('off')
        plt.show()
