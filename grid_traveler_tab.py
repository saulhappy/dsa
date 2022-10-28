"""
Say that you are a traveler on a 2D grid. You being in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Write a function `grid_traveler(m, n)` that calculates this.

"""

"""
step 1: create a table roughly same size as input
step 2: figure out seed values. counting problems are good to start with 0. 
step 3: encode base case values. here it is that 1x1 returns 1, and any point with 0 as a col or row, also returns 0. 
step 4: starting at 0, 0 where current value should be 1, add current value to all neighbors, and repeat until the reaching the end without going out of bounds. 

"""

def grid_traveler_tab(m, n):
    if m == 0 or n == 0: return 0

    table = [0] * m
    for i in range(len(table)):
        table[i] = [0] * n
    table[0][0] = 1 # base case: only one way to exit a 1x1 grid. 

    for i in range(m):
        for j in range(n):
            current_point = table[i][j]
            if j + 1 < n: table[i][j+1] += current_point
            if i + 1 < m: table[i+1][j] += current_point
            
    return table[m-1][n-1]


print(grid_traveler_tab(0, 1)) # => 0
print(grid_traveler_tab(3, 0)) # => 0
print(grid_traveler_tab(1, 1)) # => 1
print(grid_traveler_tab(2, 3)) # => 3
print(grid_traveler_tab(3, 2)) # => 3
print(grid_traveler_tab(3, 3)) # => 6
print(grid_traveler_tab(18, 18)) # => 2333606220
