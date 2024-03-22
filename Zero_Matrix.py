from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Flag to track if the first column should be zeroed
    col0 = False
    
    # Check for zero elements and mark the corresponding row and column
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if j == 0:
                    col0 = True
                else:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    
    # Zero out rows and columns based on the marks
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Zero out the first row and first column if necessary
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[0][i] = 0
    
    if col0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix
