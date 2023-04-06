class graph:
    def __init__(self, matrix):
        self.matrix = matrix
    def tetangga(self, adj):
        return self.matrix[adj]
        

