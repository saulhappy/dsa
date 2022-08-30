""" search input array presence of number """

def binary_search_i(arr, num):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(binary_search_i([-1, 0, 3, 5, 9, 12], 0)) # => True
print(binary_search_i([-1, 0, 3, 5, 9, 12], 88)) # => False
