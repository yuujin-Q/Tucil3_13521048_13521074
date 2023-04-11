"""
:file: utils.py

Some methods to support implementations of other classes
"""

from math import *


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    calculates haversine distance between two geographical points

    :param lat1: latitude of first point
    :param lon1: longitude of first point
    :param lat2: latitude of second point
    :param lon2: longitude of second point
    :return: distance between two point
    """
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 6371 * (2 * asin(sqrt(a)))


def is_square(matrix, n):
    """
    check if a matrix is square

    :param matrix:
    :param n: size of matrix to be validated
    :return: boolean of validity
    """
    return all(len(i) == n for i in matrix) and len(matrix) == n


def validate_int_input(min_value, max_value, choices=""):
    """
    loop and validate integer input between a range

    :param min_value: minimum value of range
    :param max_value: maximum value of range
    :param choices: choices prompt
    :return: valid integer
    """
    print(choices)

    is_valid = False
    input_value = 0
    while not is_valid:
        input_value = input("Ketik angka: ")
        try:
            input_value = int(input_value)
            if min_value <= input_value <= max_value:
                is_valid = True
            else:
                print("Masukan tidak valid")
        except ValueError:
            print("Masukan tidak valid")

    return input_value
