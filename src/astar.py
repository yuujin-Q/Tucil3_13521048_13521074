from graph_reader import *
import collections

class Astar(GraphReader):
    def __init__(self):
        super().__init__()

        self.adjList = collections.defaultdict(list)
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j] != 0:
                    self.adjList[i].append((j, self.adjMatrix[i][j]))

        self.h = dict()
        for i in range(len(self.adjMatrix)):
            (self.h)[i] = 1

    def heuristic(self, idx):
        return self.h[idx]


                

