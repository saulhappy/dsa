"""
Write a function 'can_sum(target_sum, numbers)' that takes in a target_sum and an array of numbers as arguments. 

The function should return a boolean indicating whether or not is is possible to generate the target_sum using the numbers from the array. 

You may use an element of the array as many times as needed. You may assume that all input numbers are non-negative. 
"""

def tab_can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum):
        if table[i] is True:
            for num in numbers:
                if (i + num) < len(table): 
                    table[i + num] = True
    
    return table[target_sum]


print(tab_can_sum(7, [5, 3, 4, 7])) # => True
print(tab_can_sum(8, [2, 3, 5])) # => True
print(tab_can_sum(7, [2, 4])) # => False
print(tab_can_sum(300, [7, 14])) # => False
