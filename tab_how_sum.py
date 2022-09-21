"""
Write a function how_sum that takes in a target_sum and an array of numbers as arguments. 
The function should return an array containing any combination of elements that add up to exactly the target_sum. 
If there is no combination that adds up to the target_sum, return null. 
If there are multiple combinations possible, you may return any single one. 

e.g. how_sum(7, [5, 3, 4, 7]) => [3, 4] or [7]
how_sum(8, [2, 3, 5]) => [2, 2, 2, 2] or [3, 5]
how_sum(7, [2, 4]) => null
how_sum(0, [1, 2, 3]) => []
"""


def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if i + num < len(table):
                    table[i + num] = table[i].copy() + [num]

    return table[target_sum]


print(how_sum(7, [2, 3])) # => [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7])) # => [4, 3]
print(how_sum(7, [2, 4])) # => None
print(how_sum(8, [2, 3, 5])) # => [2,2,2,2]
print(how_sum(300, [7, 14])) # => None
