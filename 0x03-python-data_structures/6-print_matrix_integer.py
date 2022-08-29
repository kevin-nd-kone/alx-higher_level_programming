#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("{}".format(""))
    else:
        for line in matrix:
            row = ""
            for num in line:
                row += ' {}'.format(num)
            print("{}".format(row))

print_matrix_integer()