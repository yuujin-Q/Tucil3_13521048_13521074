import os
from utils import *
from graph import LocationGraph

class GraphReader:
    def __init__(self):
        self.latitude = []
        self.longitude = []
        self.location_name = []
        self.coordinate_tuple = []
        self.adj_matrix = []
        self.filename = ""

    class GraphReaderException(Exception):
        pass

    def read_graph_file(self):
        successful_read = False
        while not successful_read:
            try:
                self._read_file()
                successful_read = True
            except self.GraphReaderException as e:
                print(e.args[0])

    def _read_file(self):
        # Detect file
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace('src', 'test')
        os.chdir(dir)
        dir += "/"

        print("Masukkan nama file (dari folder test): ", end="")
        filename = input()
        filename = dir + filename
        if not (os.path.isfile(filename)):
            raise self.GraphReaderException("File tidak ditemukan.")
        
        # Read all of file
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.read()
            result = lines.split('\n~\n') # Pembacaan koordinat dan adjMatrix dipisahkan dengan simbol '~'

        # Read coordinates
        result_coordinates = result[0]
        node_coordinates = result_coordinates.splitlines(False)

        # Put names, latitudes, longitudes in separate lists
        location_name = []
        latitude = []
        longitude = []
        for coord in node_coordinates:
            splited_line = coord.split()
            if len(splited_line) == 3:
                location_name.append(splited_line[0])
                latitude.append(float(splited_line[1]))
                longitude.append(float(splited_line[2]))        
            else:
                raise self.GraphReaderException("Simpul harus didefinisikan dalam format '<nama> <latitude> <longitude>' sebelum mendefinisikan matriks.")
                
        # Add tuple of names, latitudes, longitudes
        coordinate_tuple = []
        for i in range(len(latitude)):
            coordinate_tuple.append((location_name[i], latitude[i], longitude[i]))

        # Read adjacency matrix
        try:
            result_matrix = result[1]
        except:
            raise self.GraphReaderException("File tidak berisi pemisah '~', matriks ketetanggaan tidak dapat dibaca.")
        
        matrix_rows = result_matrix.splitlines(False) 
        adj_matrix = [[float(num) for num in row.split(' ')] for row in matrix_rows]
        if (not is_square(adj_matrix, len(location_name))):
            raise self.GraphReaderException("Matriks ketetanggaan harus persegi dan berukuran sama dengan jumlah simpul.")
        else:
            # Calculate haversine distance for those that are not valued 0
            for i in range(len(adj_matrix)):
                for j in range(len(adj_matrix[i])):
                    if adj_matrix[i][j] != 0:
                        adj_matrix[i][j] = haversine_distance(latitude[i], longitude[i], latitude[j], longitude[j])

        # commit read
        self.latitude = latitude
        self.longitude = longitude
        self.location_name = location_name
        self.coordinate_tuple = coordinate_tuple
        self.adj_matrix = adj_matrix
        self.filename = filename

    def print_reader_info(self):
        print("Nama lokasi:")
        for i in range(len(self.location_name)):
            print("%d. %s" %(i+1, self.location_name[i]))

    def get_location_graph(self):
        result = LocationGraph()
        
        # add nodes
        location_count = len(self.location_name)
        for i in range(location_count):
            result.add_node(self.location_name[i], self.latitude[i], self.longitude[i])

        # add edges
        for i in range(location_count):
            for j in range(location_count):
                edge_weight = self.adj_matrix[i][j]
                if edge_weight > 0:
                    result.add_weighted_edge(self.location_name[i], self.location_name[j], edge_weight)

        return result
    