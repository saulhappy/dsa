"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0

    while True: 
        try:
            nums[i + 1]
        except IndexError:
            break
        if nums[i] == nums[i + 1]:
            del nums[i + 1]
        else:
            i += 1
    return len(nums)

print(remove_duplicates([1, 1, 2])) # -> 2
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4])) # -> 5
print(remove_duplicates([0,0,0,0,0,0,0,0,0])) # -> 1
