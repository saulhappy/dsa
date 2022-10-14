"""
source: https://leetcode.com/problems/running-sum-of-1d-array/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

def running_sum(nums):
    result = []

    for i in range(len(nums)):
        if i == 0:
            result.append(nums[i])
        else:
            result.append(result[i - 1] + nums[i])
    return result

print(running_sum(nums = [1, 2, 3, 4]))
