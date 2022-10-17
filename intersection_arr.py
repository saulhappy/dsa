"""
source: https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

"""


def intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))

print(intersection([1,2,2,1], [2,2])) # -> [2,2]
print(intersection([4,9,5], [9,4,9,8,4])) # -> [4,9] or [9,4]

