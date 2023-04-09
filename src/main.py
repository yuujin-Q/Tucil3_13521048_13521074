from graph import *
from graph_reader import *
from route_planner import *

reader = GraphReader()
reader.read_graph_file()

print("Pilih algoritma yang ingin digunakan:")
print("1. Algoritma UCS")
print("2. Algoritma A*")
isValid = False
while (not isValid):
    print("Ketik angka: ", end="")
    choice = input()
    if (choice == "1" or choice == "2"):
        isValid = True
    else:
        print("Masukan tidak valid.")


reader.print_reader_info()

my_graph = reader.get_location_graph()

# my_graph.display_graph(with_weights=False)

# print(astar_graph.h)
# print(astar_graph.adjList)

print("Pilih kota awal")
isValid = False
while (not isValid):
    print("Ketik angka: ", end="")
    awal = int(input())
    if not 1 <= awal <= len(reader.coordinateTuple):
        print("Masukan tidak valid.")
    else:
        isValid = True

print("Pilih kota akhir")
isValid = False
while (not isValid):
    print("Ketik angka: ", end="")
    akhir = int(input())
    if not 1 <= akhir <= len(reader.coordinateTuple):
        print("Masukan tidak valid.")
    else:
        isValid = True

# if choice == "1":
#     print()
#     ucs_graph = UCS(my_graph, True)
#     ucs_graph.ucs_search(reader.locationName[awal - 1], reader.locationName[akhir - 1])
#     print()
#     ucs_graph.print_solution()
# else:
#     print()
#     astar_graph = AStar(reader, awal - 1, akhir - 1)
#     path, distance = astar_graph.astar_search(reader)

use_astar = False if choice == "1" else True

solver = RoutePlanner(my_graph, with_astar_heuristic=use_astar, show_debug=True)
print(solver.get_solution())
solver.plan_route(reader.locationName[awal - 1], reader.locationName[akhir - 1])
print()
solver.print_solution()