"""
write a function best_sum(target_sum, numbers) that takes in a target_sum and array of numbers as arguments.
The function should return an array containing the SHORTEST combination of numbers that add up to exactly the target_sum. 
If there is a time for the shortest combination, you may return any one of the shortest. 

best_sum(7, [5, 3, 4, 7]) => [7]
best_sum(8, [2, 3, 5]) => [3, 5]

"""

def tab_best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    
    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i + num < len(table):
                    current_combination = table[i].copy() + [num]
                    # if current combination is shorter than what is already stored, replace
                    if (table[i+num] is None) or (len(table[i + num]) > len(current_combination)):
                        table[i + num] = table[i].copy() + [num]
    return table[target_sum]


print(tab_best_sum(7, [5, 3, 4, 7])) # => [7]
print(tab_best_sum(8, [2, 3, 5])) # => [3, 5]
print(tab_best_sum(8, [1, 4, 5])) # => [4, 4]
print(tab_best_sum(100, [25, 2, 1, 5])) # => [25, 25, 25, 25]
