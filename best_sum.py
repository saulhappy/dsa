"""
write a function bestSum(targetSum, numbers) that takes in a targetsum and array of numbers as arguments.
The function should return an array containing the SHORTEST combination of numbers that add up to exactly the targetSum. 
If there is a time for the shortest combination, you may return any one of the shortest. 

bestSum(7, [5, 3, 4, 7]) => [7]
bestSum(8, [2, 3, 5]) => [3, 5]

"""

def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortest_complements = None
    combination = None

    for num in numbers:
        complement = targetSum - num
        complements = bestSum(complement, numbers)

        if complements != None:
             combination = complements + [num]
        if shortest_complements == None or len(combination) < len(shortest_complements):
            shortest_complements = combination
    return shortest_complements


def bestSumMemo(targetSum, numbers, memo = {}):
    if targetSum in memo:
        return memo[targetSum] 
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortest_complements = None
    combination = None

    for num in numbers:
        complement = targetSum - num
        complements = bestSumMemo(complement, numbers, memo)

        if complements != None:
             combination = complements + [num]
        if shortest_complements == None or len(combination) < len(shortest_complements):
            shortest_complements = combination

    memo[targetSum] = shortest_complements
    return shortest_complements

"""
target sum: m
n : len(numbers)

Brute force:
time: O(n^m * m)
space: O(m^2)

Memoized:
time: O(m^2 * n )
space: O(m^2)

"""

# print(bestSum(7, [5, 3, 4, 7])) # => [7]
# print(bestSum(8, [2, 3, 5])) # => [3, 5]
# print(bestSum(8, [1, 4, 5])) # => [4, 4]
# print(bestSum(100, [1, 2, 5, 25])) # => [25, 25, 25, 25]

print(bestSumMemo(100, [1, 2, 5, 25])) # => [25, 25, 25, 25]


