from graph_reader import *
from utils import *
import collections

class Astar():
    def __init__(self, graph_reader, src, dest):

        self.adjList = collections.defaultdict(list)
        for i in range(len(graph_reader.adjMatrix)):
            for j in range(len(graph_reader.adjMatrix[i])):
                if graph_reader.adjMatrix[i][j] != 0:
                    self.adjList[i].append((j, graph_reader.adjMatrix[i][j]))

        self.awal = src
        self.tujuan = dest

        self.h = dict()
        for i in range(len(graph_reader.adjMatrix)):
            (self.h)[i] = haversine_distance(graph_reader.latitude[i], graph_reader.longitude[i], graph_reader.latitude[dest], graph_reader.longitude[dest])

    def heuristic(self, idx):
        return self.h[idx]

    def astar_search(self, graph_reader):
        adjMap = {}
        adjMap[self.awal] = self.awal
        distanceMap = {}
        distanceMap[self.awal] = 0
        totaldistance = 0
        list1 = [self.awal]
        list2 = []

        while len(list1) > 0:
            n = None
            for i in list1:
                if (n == None) or (distanceMap[i] + self.heuristic(i) < distanceMap[n] + self.heuristic(n)):
                    n = i
            if n == None:
                print("Rute terpendek tidak ditemukan.")
                return None, None
            for (x, y) in self.adjList[n]:
                if (x not in list1 and x not in list2):
                    list1.append(x)
                    adjMap[x] = n
                    distanceMap[x] = distanceMap[n] + y
                else:
                    if distanceMap[x] > distanceMap[n] + y:
                        distanceMap[x] = distanceMap[n] + y
                        adjMap[x] = n
                        if x in list2:
                            list2.remove(x)
                            list1.append(x)
            list1.remove(n)
            list2.append(n)
            if n == self.tujuan:
                totaldistance = distanceMap[n]
                solution = []
                while adjMap[n] != n:
                    solution.append(graph_reader.locationName[n])
                    n = adjMap[n]
                solution.append(graph_reader.locationName[self.awal])
                solution.reverse()
                print(f"Solution Path = {solution}")
                print(f"Solution Total Cost = {totaldistance}")
                return solution, totaldistance
        print("Rute terpendek tidak ditemukan.")
        return None, None

                

