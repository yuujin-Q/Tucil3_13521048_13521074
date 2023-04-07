from queue import PriorityQueue
from graph import LocationGraph

class UCS():
    graph = LocationGraph()
    solution_cost = 0
    solution_path = []

    def __init__(self, graph, show_debug=False):
        self.graph = graph
        self.show_debug = show_debug

    def ucs_search(self, start_node_name, finish_node_name):
        """UCS Search Algorithm
        :param start_node_name: string of starting node name
        :param finish_node_name: string of finish node (goal)

        :return: boolean of search success
        """
        next_search = PriorityQueue()

        # definition: node = (name, path_taken)
        start_node = (start_node_name, [])

        # enqueue start_node; priority = total_cost in route
        next_search.put((0, start_node))
        explored = set()
        
        while not next_search.empty():
            # dequeue current node to search
            current_cost, current_node = next_search.get()
            
            # setup: get current node name and current node path (include current name as visited in path)
            current_node_name = current_node[0]
            current_node_path = current_node[1] + [current_node_name]

            # show debug messages
            if self.show_debug is True:
                print("Current (cost, name, path): ", end='')
                print(current_cost, current_node_name, current_node_path)

            # goal check
            if current_node_name == finish_node_name:
                self.solution_path = current_node_path
                self.solution_cost = current_cost

                # search success
                return True
            
            # mark node name as visited
            explored.add(current_node[0])
            
            # enqueue neighbors
            for neighbor_name in self.graph.get_neighbors(current_node_name):
                if neighbor_name not in explored:
                    neighbor_cost = current_cost + self.graph.get_edge_cost(current_node_name, neighbor_name)
                    neighbor_path = current_node_path

                    new_neighbor_node = (neighbor_name, neighbor_path)

                    next_search.put((neighbor_cost, new_neighbor_node))
        
        # Search failed
        return False
    
    def get_solution(self):
        """
        :return: tuple of instance's latest solution cost and solution path
        """
        return self.solution_cost, self.solution_path
    
    def print_solution(self):
        """prints latest solution cost and solution path"""
        print(f"Solution Path = {self.solution_path}")
        print(f"Solution Total Cost = {self.solution_cost}")
