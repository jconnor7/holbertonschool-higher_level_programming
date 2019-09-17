#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) is not 0:
            for j in row[:-1]:
                """return list w/o last element"""
                print("{:d}".format(j), end=" ")
            print("{:d}".format(row[-1]), end="")
            """print w/o space"""
        print("")
