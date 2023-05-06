import csv
from hashmap import HashMap
from package import Package


def map_csv():  # Creates a HashMap of the Package Data held in inputs.csv
    with open('./inputs/inputs.csv', encoding='utf-8-sig') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=",")
        h = HashMap()
        for row in read_csv:
            p = Package()
            i = 0
            for element in row:
                p.set[i] = element
                i += 1
            h.add(p.set[0], p)
        return h


def create_matrix():  # Creates a 2D Matrix of the table from distanceData.csv
    with open('./inputs/distanceData.csv', encoding='utf-8-sig') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=",")
        mat = []
        for row in read_csv:
            mat.append(row)
        return mat
