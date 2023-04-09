from math import *

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    return (6371 * (2 * asin(sqrt(a))))

def is_square(matrix, n):
    return all(len(i) == n for i in matrix) and len(matrix) == n

def validate_int_input(min_value, max_value, choices=""):
    print(choices)

    is_valid = False
    while not is_valid:
        input_value = input("Ketik angka: ")
        try:
            input_value = int(input_value)
            if min_value <= input_value <= max_value:
                is_valid = True
            else:
                print("Masukan tidak valid")
        except:
            print("Masukan tidak valid")
    
    return input_value