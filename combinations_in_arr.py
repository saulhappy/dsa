"""
get all possible combinations of input array

"""

def combinations(arr):
    if len(arr) == 0: return [[]]
    first_element = arr[0]
    other_elements = arr[1:]

    combinations_without_first_element = combinations(other_elements)
    combinations_with_first_element = []

    for combination in combinations_without_first_element:
        combination_with_first_element = combination + [first_element]
        combinations_with_first_element.append(combination_with_first_element)
    
    return combinations_without_first_element + combinations_with_first_element

"""
Time: O(2^n) => binary choices for each element of array 
Space: O(n^2) call stacks x n - 1 arrays per stack, n * n-1 
"""


print(combinations(['a', 'b', 'c']))
# =>
# [
#     [],
#     ['a'],
#     ['b'],
#     ['c'],
#     ['a', 'b'],
#     ['b', 'c'],
#     ['a', 'c'],
#     ['a', 'b', 'c']
# ]
print("============================")
print(combinations([])) # => [[]]

print("============================")

print(combinations(['b', 'c']))
