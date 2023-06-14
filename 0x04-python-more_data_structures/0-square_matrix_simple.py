#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    
    # Fill the new matrix with the square of each value in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2
    
    return result
