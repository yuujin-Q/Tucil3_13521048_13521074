import os
from astar import Astar

def readFile(file):
    # Asumsikan semua elemen matrix pada file memiliki tipe float
    # Asumsikan juga matrix tidak perlu berbentuk square
    with open(file, 'r') as f:
        l = [[float(num) for num in line.split(' ')] for line in f]
    return l

def isSquare(matrix):
    return all(len(i) == len(matrix) for i in matrix)

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('src', 'test')
os.chdir(dir)
matrix = readFile('test1.txt')
print(matrix)

if (isSquare(matrix)):
    print("yes")
else:
    print("no")

# Kenapa error ya kalau dijalanin?
# as = Astar(matrix)
# print(as.getadjList)
# print(as.geth) 






