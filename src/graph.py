import networkx as nx

"""LocationGraph: a wrapper class for nx.DiGraph (NetworkX's Directed Graph)"""
class LocationGraph(nx.DiGraph):
    """constructor"""
    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)

    """SETTERS (add nodes, edges)"""
    """add new node override"""
    def add_node(self, node_name, latitude=0, longitude=0):
        super().add_node(node_name, lat=latitude, lon=longitude)

    """add weighted edge override"""
    def add_weighted_edges_from(self, start_node_name, finish_node_name, weight):
        return super().add_weighted_edges_from([(start_node_name, finish_node_name, weight)])

    """GETTERS"""    
    """get neighbors"""
    def get_neighbors(self, n):
        # return iterator to neighbors of n
        return super().neighbors(n)
    
    """get nodes"""
    def get_nodes(self):
        # return iterator to nodes of graph
        return super().nodes()

    """get edges"""
    def get_edges(self):
        # return iterator to edges of graph
        return super().edges()
    
    """get edge cost"""
    def get_edge_cost(self, start_node_name, finish_node_name):
        cost = self.get_edge_data(start_node_name, finish_node_name);
        if cost == None:
            return float('inf')
        else:
            return cost
        
    """heuristic function"""
    def get_distance_between(self, start_node_name, finish_node_name):
        # check for invalid node parameter
        if (not self.has_node(start_node_name)) or (not self.has_node(finish_node_name)):
            return float('inf')
        else:
            # temporary implementation, euclidean distance
            node_1 = self.nodes[start_node_name]
            node_2 = self.nodes[finish_node_name]

            cost = (node_2['lat'] - node_1['lat']) ** 2 + (node_2['lon'] - node_1['lon']) ** 2

            return cost ** 0.5
    