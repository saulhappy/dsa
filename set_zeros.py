"""
source: https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

"""

"""
algo1totry:
for each num in each arr of the matrix:
    if the number is zero:
        make note of the index the zero is in that arr
        to make that column all all zeros:
            make each number in all of the arrays of the matrix that matches that index a zero
        to make that row a zero:
            make the entire array the zero is in zeros

Gotchas: how to deal with multiple zeros?

"""

def make_row_zeros(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] = 0
    return arr

def set_zeros(matrix):
    indices_to_zero = []

    for arr in matrix:
        for i in range(len(arr)):
            if arr[i] == 0:
                indices_to_zero.append(i)

    for arr in matrix:
        for i in range(len(arr)):
            if arr[i] == 0: 
                arr = make_row_zeros(arr) # make entire row 0
                break
    for arr in matrix:
        for i in range(len(arr)):
            if i in indices_to_zero and arr[i] != 0:
                arr[i] = 0
    return matrix


print(set_zeros([[1,1,1],[1,0,1],[1,1,1]])) # -> [[1,0,1],[0,0,0],[1,0,1]]
print(set_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
