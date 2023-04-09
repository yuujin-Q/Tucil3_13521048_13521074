from graph import *
from graph_reader import *
from route_planner import *
from utils import *

# select and read map file
reader = GraphReader()
reader.read_graph_file()

# select algorithm choice (UCS/A*)
algorithm_choice_prompt = (
    "Pilih algoritma yang ingin digunakan:\n"
    "1. Algoritma UCS\n"
    "2. Algoritma A*"
)
algorithm_choice = validate_int_input(1, 2, algorithm_choice_prompt)
use_astar = False if algorithm_choice == 1 else True
print()

# show locations, select start and finish point of search
reader.print_reader_info()
start_index = validate_int_input(1, len(reader.coordinate_tuple), "Pilih tujuan awal")
finish_index = validate_int_input(1, len(reader.coordinate_tuple), "Pilih tujuan akhir")
print()

# start route search
print("Hasil pencarian")
location_graph = reader.get_location_graph()
solver = RoutePlanner(location_graph, with_astar_heuristic=use_astar, show_debug=False)
found_route = solver.plan_route(reader.location_name[start_index - 1], reader.location_name[finish_index - 1])
if found_route:
    solver.print_solution()
else:
    print("Rute tidak ditemukan")

location_graph.display_graph(with_weights=True, solution_path=solver.solution_path)
