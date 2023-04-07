import os
from utils import *
from graph import LocationGraph

class GraphReader:
    def __init__(self):
        self.latitude = []
        self.longitude = []
        self.locationName = []
        self.coordinateTuple = []
        self.adjMatrix = []
        self.fileName = ""

    def read_graph_file(self):
        # Detect file
        isValid = False
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace('src', 'test')
        os.chdir(dir)
        dir += "/"
        while not isValid:
            print("Masukkan nama file (dari folder test): ", end="")
            calonFileName = input()
            self.fileName = dir + calonFileName
            if (os.path.isfile(self.fileName)):
                isValid = True
            else:
                print("File doesn't exist.")
        
        # Read all of file
        with open(self.fileName, 'r', encoding='utf-8') as file:
            lines = file.read()
            result = lines.split('\n~\n') # Pembacaan koordinat dan adjMatrix dipisahkan dengan simbol '~'

        # Read coordinates
        resultCoor = result[0]
        listresultCoor = resultCoor.splitlines(False)
        allLinesCoor = []
        for lines in listresultCoor:
            allLinesCoor += lines.split()
        # Put names, latitudes, longitudes in separate lists
        for i in range(len(allLinesCoor)):
            if (i % 3 == 0):
                self.locationName.append(allLinesCoor[i])
            elif (i % 3 == 1):
                self.latitude.append(float(allLinesCoor[i]))
            else:
                self.longitude.append(float(allLinesCoor[i]))
        # Add tuple of names, latitudes, longitudes
        for i in range(len(self.latitude)):
            self.coordinateTuple.append((self.locationName[i], self.latitude[i], self.longitude[i]))

        # Read adjacency matrix
        resultMatrix = result[1]   
        listresultMatrix = resultMatrix.splitlines(False) 
        self.adjMatrix = [[float(num) for num in line.split(' ')] for line in listresultMatrix]
        if (not is_square(self.adjMatrix)):
            print("Matriks tidak berbentuk persegi. Silakan coba lagi.")
        else:
            # Calculate haversine distance for those that are not valued 0
            for i in range(len(self.adjMatrix)):
                for j in range(len(self.adjMatrix[i])):
                    if self.adjMatrix[i][j] != 0:
                        self.adjMatrix[i][j] = haversine_distance(self.latitude[i], self.longitude[i], self.latitude[j], self.longitude[j])

    def print_reader_info(self):
        print("Latitudes:")
        print(self.latitude, '\n')

        print("Longitudes:")
        print(self.longitude, '\n')

        print("Node Names:")
        print(self.locationName, '\n')

        print("Coordinates:")
        print(self.coordinateTuple, '\n')

        print("Adjacency Matrix:")
        for row in self.adjMatrix:
            print(row)

    def get_location_graph(self):
        result = LocationGraph()
        
        # add nodes
        location_count = len(self.locationName)
        for i in range(location_count):
            result.add_node(self.locationName[i], self.latitude[i], self.longitude[i])

        # add edges
        for i in range(location_count):
            for j in range(location_count):
                edge_weight = self.adjMatrix[i][j]
                if edge_weight > 0:
                    result.add_weighted_edges_from(self.locationName[i], self.locationName[j], edge_weight)


        return result
    