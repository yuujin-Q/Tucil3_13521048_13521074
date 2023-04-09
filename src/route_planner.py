from queue import PriorityQueue
from graph import LocationGraph

class RoutePlanner():
    graph = LocationGraph()
    solution_cost = float('inf')
    solution_path = []
    with_astar_heuristic = False
    show_debug = False

    def __init__(self, graph, with_astar_heuristic, show_debug=False):
        """
        :param graph: LocationGraph
        :param with_astar_heuristic: astar heuristic boolean toggle
        :param show_debug: debug message toggle
        """
        self.graph = graph
        self.with_astar_heuristic = with_astar_heuristic
        self.show_debug = show_debug

    class SearchNode():
        def __init__(self, name, path_list, path_cost) -> None:
            """
            :param name: string of instance location name
            :param path_list: list of location name strings 'visited' by instance
            :param path_cost: total cost of path taken by instance 
            """
            self.name = name
            self.path_list = [location for location in path_list]
            self.path_cost = path_cost
        
        def add_self_to_path_list(self):
            self.path_list = self.path_list + [self.name]
            

    def plan_route(self, start_node_name, finish_node_name):
        """UCS/AStar Search Algorithm
        :param start_node_name: string of starting node name
        :param finish_node_name: string of finish node (goal)

        :return: boolean of search success
        """

        # SETUP: priority queue, starting node, explored nodes
        search_pqueue = PriorityQueue()
        starting_node = self.SearchNode(start_node_name, [], 0)

        # enqueue start_node; if is using astar, priority considers the heuristic value
        if self.with_astar_heuristic is True:
            node_priority = starting_node.path_cost + self.graph.get_distance_between(starting_node.name, finish_node_name)
        else:
            node_priority = starting_node.path_cost

        search_pqueue.put((node_priority, starting_node))
        explored_node_names = set()
        
        # SEARCH: do search loop
        while not search_pqueue.empty():
            # dequeue current node to search
            node_priority, current_node = search_pqueue.get()
            current_node.add_self_to_path_list()

            # show debug messages
            if self.show_debug is True:
                print(node_priority, "---", current_node.name, "--", current_node.path_cost, current_node.path_list)

            # Goal check: return from function if goal is met
            if current_node.name == finish_node_name:
                self.solution_path = current_node.path_list
                self.solution_cost = current_node.path_cost

                return True     # search success
            
            # mark current node name as visited
            explored_node_names.add(current_node.name)
            
            # enqueue neighbors
            for neighbor_name in self.graph.get_neighbors(current_node.name):
                if neighbor_name not in explored_node_names:
                    neighbor_cost = current_node.path_cost + self.graph.get_edge_cost(current_node.name, neighbor_name)

                    new_neighbor_node = self.SearchNode(neighbor_name, current_node.path_list, neighbor_cost)

                    if self.with_astar_heuristic is True:
                        node_priority = neighbor_cost + self.graph.get_distance_between(neighbor_name, finish_node_name)
                    else:
                        node_priority = neighbor_cost

                    search_pqueue.put((node_priority, new_neighbor_node))
        
        # Search failed
        return False
    
    def get_solution(self):
        """
        :return: tuple of instance's latest solution cost and solution path
        """
        return self.solution_cost, self.solution_path
    
    def print_solution(self):
        print(f"Solution Path = {self.solution_path}")
        print(f"Solution Total Cost = {self.solution_cost}")

    def reset_solution(self):
        self.solution_cost = float('inf')
        self.solution_path = []

