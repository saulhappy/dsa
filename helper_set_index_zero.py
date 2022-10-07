def set_index_zero(matrix, index):
    for arr in matrix:
        for i in range(len(arr)):
            if i == index and arr[i] != 0:
                arr[i] = 0
    return matrix


print(set_index_zero([[1,1,1],[1,0,1],[1,1,1]], 1)) # -> [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
