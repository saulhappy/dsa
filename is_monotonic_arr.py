""" source: https://leetcode.com/problems/monotonic-array/#:~:text=An%20array%20is%20monotonic%20if,%3E%3D%20A%5Bj%5D%20."""

"""
algorithm: is the sorted arr equal to the arr? 
or is the reverse sorted arr equal to the arr?
"""
def is_monotonic(arr):
    return sorted(arr) == arr or arr == sorted(arr, reverse=True)

print(is_monotonic([1, 2, 3, 4, 5])) # True
print(is_monotonic([1, 2, 1, 4, 5])) # False
print(is_monotonic([10, 9, 8, 7, 6])) # True
print(is_monotonic([1, 2, 3, 4, 5])) # True

