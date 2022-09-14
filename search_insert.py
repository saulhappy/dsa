"""
# source: https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

"""

def search_insert(nums, target):
    # case where target is in nums
    if target in nums:
        return nums.index(target)
    # case where target is not in nums, and larger than anything in array
    elif target > nums[len(nums) - 1]:
        return len(nums)
    # case where target is not in nums, and smaller than anything in array
    elif target < nums[0]:
        return 0
    # case where target is not in nums, and should be somewhere in the middle
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                return i

# Similar algorithm: Itaerate. If the target is in the array, return i. Else, return the length of it. 
# for i in range(len(nums)):
#     if target <= nums[i]:
#         return i
# return len(nums)

# Both are O(n), but can achieve faster binary search solution of O(logN), sacrificing space O(1)


def search_insert_binary(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1 # target might be at left of array
        else:
            left = mid + 1 
    return left # at end of iteration, if target wasn't found, left position is where it ought to be. 


print(search_insert([1], 0)) # => 0
print(search_insert([1,3,5,6], 2)) # => 1
print(search_insert([1,3,5,6], 7)) # => 4
print(search_insert([1,3,5,6], 5)) # => 2
print(search_insert([1,3,5,6], 0)) # => 0
