def is_different_sign(num1, num2):
    if num1 * num2 < 0:
        return True
    return False

def circular_array_loop(nums):
    slow = 0
    fast = 0

    for i in range(len(nums)):
        if slow == i and fast == i:
            return True
        else:
            slow = nums[slow]
            fast = nums[slow]
            fast = nums[fast+1]
    
    return False


# TEST CASES

print(circular_array_loop([1,3,-2,-4,1])) # => True

print(circular_array_loop([2,1,-1-2,2])) # => False

# print(circular_array_loop([3,3,1,-1,2])) # => True
