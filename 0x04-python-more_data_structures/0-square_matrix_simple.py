#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[i])):
            temp_list.append(matrix[i][j]**2)
        my_list.append(temp_list)
    return my_list
