from graph import *

myGraph = LocationGraph()

myGraph.add_node("ITB", 0, 0)
myGraph.add_node("bonbin", 10, 10)
myGraph.add_node("kfc", -10, 15)
myGraph.add_node("saraga", 20, 16)

myGraph.add_weighted_edges_from("ITB", "kfc", 50)
myGraph.add_weighted_edges_from("ITB", "saraga", 20)
myGraph.add_weighted_edges_from("kfc", "saraga", 20)
myGraph.add_weighted_edges_from("kfc", "bonbin", 10)

print(list(myGraph.get_nodes()))
print(list(myGraph.get_edges()))
print(myGraph.get_edge_cost("kfc", "ITB"))
print(myGraph.get_edge_cost("ITB", "kfc"))
print(myGraph.get_edge_cost("kfc", "I"))
print(myGraph.get_distance_between("ITB", "bonbin"))
print(myGraph.get_distance_between("ITB", "sar"))
print(myGraph.get_distance_between("bonbin", "saraga"))