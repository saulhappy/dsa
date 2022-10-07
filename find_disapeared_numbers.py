"""
SOURCE: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""

def find_disappeared_numbers(nums):
    result = []
    for num in nums:
        x = abs(num) - 1
        if nums[x] > 0: nums[x] *= -1
    
    for i in range(len(nums)):
        if nums[i] > 0: result.append(i+1)
    return result 

print(find_disappeared_numbers([2,2])) # => [1]
print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) # => [5,6]
print(find_disappeared_numbers([1,1])) # => [2]
