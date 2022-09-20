"""
Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
the non-zero elements.

"""

def move_zeros(arr):

    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr


print(move_zeros([0,1,0,3,12])) # => [1, 3, 12, 0, 0]
print(move_zeros([1,7,0,0,8,0,10,12,0,4])) # => [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
