from graph import *
from graph_reader import *
from ucs import *

reader = GraphReader()
reader.read_graph_file()
reader.print_reader_info()

my_graph = reader.get_location_graph()

# my_graph.display_graph(with_weights=False)

print()
ucs_graph = UCS(my_graph, True)
ucs_graph.ucs_search("braga","celengan")
print()
ucs_graph.print_solution()
