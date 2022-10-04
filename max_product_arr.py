"""
source: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
"""

def max_product_arr(nums):
    numsSorted = sorted(nums)
    return (numsSorted[-1] - 1) * (numsSorted[-2] - 1)


print(max_product_arr([3,4,5,2])) # -> 12
