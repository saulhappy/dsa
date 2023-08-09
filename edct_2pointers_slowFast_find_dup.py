# from collections import Counter

# def find_duplicate(nums):
#     nums_map = Counter(nums)

#     for k, v in nums_map.items():
#         if v >= 2:
#             return k


def find_duplicate(nums):
    fast = slow = nums[0]
  
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
   
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast



# TEST CASES:

print(find_duplicate([1, 5, 4, 3, 2, 4, 6])) # => 4

print(find_duplicate([5, 6, 1, 3, 7, 3, 2, 4, 8])) # => 3

print(find_duplicate([2, 10, 6, 7, 11, 7, 9, 4, 3, 8, 5, 1])) # => 7

print(find_duplicate([9, 6, 12, 7, 15, 8, 3, 13, 2, 10, 4, 14, 1, 11, 9, 5])) # => 9


