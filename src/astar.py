from graph import graph
import collections

class Astar(graph):
    def __init__(self, matrix):
        super().__init__(matrix)

        self.adjList = collections.defaultdict(list)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    self.adjList[i].append((j, self.matrix[i][j]))

        self.h = dict()
        for i in range(len(self.matrix)):
            (self.h)[i] = 1

    def heuristic(self, idx):
        return self.h[idx]


                

