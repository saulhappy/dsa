"""
Write a function howSum that takes in a targetSum and an array of numbers as arguments. 
The function should return an array containing any combination of elements that add up to exactly the targetSum. 
If there is no combination that adds up to the targetSum, return null. 
If there are multiple combinations possible, you may return any single one. 

e.g. howSum(7, [5, 3, 4, 7]) => [3, 4] or [7]
howSum(8, [2, 3, 5]) => [2, 2, 2, 2] or [3, 5]
howSum(7, [2, 4]) => null
howSum(0, [1, 2, 3]) => []
"""



def how_sum_recr(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        complement = targetSum - num
        complement_result = how_sum_recr(complement, numbers)
        if complement_result != None:
            return complement_result + [num]
    return None

# print(how_sum_recr(7, [2, 3])) # => [3, 2, 2]
# print(how_sum_recr(7, [5, 3, 4, 7])) # => [4, 3]
# print(how_sum_recr(7, [2, 4])) # => None
# print(how_sum_recr(8, [2, 3, 5])) # => [2, 2, 2, 2]
# print(how_sum_recr(0, [1, 2, 3])) # => []
# print(how_sum_recr(300, [7, 14])) # => takes way too long


def how_sum_memo(targetSum, numbers, memo = {}):
    if targetSum in memo: 
        return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        complement = targetSum - num
        complement_result = how_sum_memo(complement, numbers, memo)
        if complement_result != None:
            memo[targetSum] =  complement_result + [num]
            return memo[targetSum]

    memo[targetSum] = None        
    return None

print(how_sum_memo(8, [2, 3, 5])) # => [2, 2, 2, 2]
print(how_sum_memo(300, [7, 14])) # => [2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]


"""
target sum: m
n : len(numbers)

Brute force:
time: O(n^m*m)
space: O(m)

Memoized:
time: O(n*m^2) => quadratic
space: O(m)

"""
