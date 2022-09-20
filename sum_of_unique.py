"""
source:https://leetcode.com/problems/sum-of-unique-elements/

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

"""

def sum_of_unique(arr):
    arr_map = {}
    result = 0

    for num in arr:
        if num in arr_map:
            arr_map[num] += 1
        else:
            arr_map[num] = 1
    
    for (key, value ) in arr_map.items():
        if value == 1:
            result += key
    
    return result

# MORE PYTHONIC: return sum(digit for digit in nums if nums.count(digit) == 1)

print(sum_of_unique([1,2,3,2])) # => 4  
print(sum_of_unique([1,1,1,1,1])) # => 0
print(sum_of_unique([1,2,3,4,5])) # => 15
