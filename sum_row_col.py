"""
source: https://www.youtube.com/watch?v=UbBCg0-xjkU
Write a program that reads a 5x5 array of integers and then prints the row sum and column sum. 

arr = [
    [8,3,9,0,10],
    [3,5,17,1,1],
    [2,8,6,23,1],
    [15,7,3,2,9],
    [6,14,2,6,0]
]
=> row total: 30, 27, 40, 36, 28
=> column total: 34, 37, 37, 32, 21
"""

arr = [
    [8,3,9,0,10],
    [3,5,17,1,1],
    [2,8,6,23,1],
    [15,7,3,2,9],
    [6,14,2,6,0]
]

def sum_row_col(arr):
    row_total = []
    col_total = []
    for row in arr:
        row_total.append(sum(row))
    for i in range(len(arr)):
        curr_col =[arr[0][i]]
        for j in range(1, 5):
            curr_col.append(arr[j][i])
        col_total.append(sum(curr_col))
    
    return f"row total: {row_total} \ncolumn total: {col_total}"
            

print(sum_row_col(arr))
