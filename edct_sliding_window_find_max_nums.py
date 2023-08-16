"""
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.
"""

# O(n x w) solution. For an O(n) solution: https://leetcode.com/problems/sliding-window-maximum/solutions/3915849/fast-o-n-deque/

def find_max_sliding_window(nums, w):
    result = []

    for i in range(len(nums)):
        curr_window = nums[i:w]
        result.append(max(curr_window))
        w += 1
        if w > len(nums):
            break
    return result


# TEST CASES

print(find_max_sliding_window(nums=[1,3,-1,-3,5,3,6,7], w=3)) # => [5, 5, 4, 4, 6, 7, 20]

print(find_max_sliding_window(nums=[1], w=1)) # => [5, 5, 4, 4, 6, 7, 20]

print(find_max_sliding_window(nums=[-4, 5, 4, -4, 4, 6, 7, 20], w=2)) # => [5, 5, 4, 4, 6, 7, 20]

print(find_max_sliding_window(nums=[-4, 5, 4, -4, 4 , 6, 7], w=10)) # => [7]

print(find_max_sliding_window(nums=[3, 3, 3, 3, 3, 3], w=3)) # => [3, 3, 3, 3]

print(find_max_sliding_window(nums = [1, 2, 3, 1, 4, 5, 2, 3, 6], w=3)) # => [3, 3, 4, 5, 5, 5, 6]