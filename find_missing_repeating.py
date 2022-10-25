"""
source: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

"""

def find_missing_repeating(arr):
    missing = None
    repeating = None

    arr = sorted(arr)

    # for missing
    for i in range(len(arr)):
        if arr[i+1] >= arr[i] + 2:
            missing = arr[i] + 1
            break
    
    # for repeating
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            repeating = arr[i]
            break
                    
    return f"Missing = {missing}   Repeating = {repeating}"


print(find_missing_repeating([3,1,3])) # -> missing = 2, repeating = 3
print(find_missing_repeating([4, 3, 6, 2, 1, 1])) # -> missing = 5, repeating = 1
