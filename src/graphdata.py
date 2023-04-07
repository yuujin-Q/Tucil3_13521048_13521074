import os
from utils import *

class graphdata:
    def __init__(self):
        self.latitude = []
        self.longitude = []
        self.locationName = []
        self.coordinateTuple = []
        self.adjMatrix = []
        self.fileName = ""

    def readFile(self):
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
        if (not isSquare(self.adjMatrix)):
            print("Matriks tidak berbentuk persegi. Silakan coba lagi.")
        else:
            # Calculate euclidean distance for those that are not valued 0
            for i in range(len(self.adjMatrix)):
                for j in range(len(self.adjMatrix[i])):
                    if self.adjMatrix[i][j] != 0:
                        self.adjMatrix[i][j] = euclidean(self.latitude[i], self.longitude[i], self.latitude[j], self.longitude[j])

# Try test2.txt
graf1 = graphdata()
graf1.readFile()
print(graf1.latitude)
print(graf1.longitude)
print(graf1.locationName)
print(graf1.coordinateTuple)
print(graf1.adjMatrix)


                

    
