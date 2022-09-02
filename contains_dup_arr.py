""" 
source: https://leetcode.com/problems/contains-duplicate/ 

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

"""
# Algo1: set a seen array. Iterate nums array. If num in seen, return True. Else
# append num to seen. Return False at end of iteration. Exceeds time. 

# Algo2: use a hash instead of array to contain seen. Accepted

nums = [1,2,3,1]

# Algo1: 
# def contains_duplicate(nums):
#     seen = []
#     for num in nums:
#         if num in seen: return True
#         else: seen.append(num)
#     return False

# Algo2: 
def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen: return True
        else: seen[num] = 1
    return False

print(contains_duplicate(nums))
