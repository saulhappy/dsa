"""
source: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

"""

def max_sub_array(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i] + current_sum, nums[i])
        max_sum = max(current_sum, max_sum)
    
    return max_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4])) # -> 6
print(max_sub_array([1])) # -> 1
print(max_sub_array([0])) # -> 0
print(max_sub_array([-1])) # -> -1 
print(max_sub_array([-100000])) # -> -100000


