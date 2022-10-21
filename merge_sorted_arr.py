""" 
source: https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

"""


def merge_sorted_arr(nums1,m,nums2,n):
    nums1[m:] = nums2
    return sorted(nums1)
    
print(merge_sorted_arr(nums1=[1,2,3,0,0,0],m=3,nums2=[2,5,6],n=3)) # -> [1,2,2,3,5,6]
print(merge_sorted_arr(nums1=[1],m=1,nums2=[],n=0)) # -> [1]
