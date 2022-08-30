""" search input array presence of number """

def binary_search_r(arr, num):
    # base case:
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != num):
        return False

    mid = arr[len(arr)// 2]

    if num == mid: return True
    if num < mid: return binary_search_r(arr[:len(arr)//2], num)
    if num > mid: return binary_search_r(arr[len(arr)//2:], num)

print(binary_search_r([-1, 0, 3, 5, 9, 12], 3)) # => True
print(binary_search_r([-1, 0, 3, 5, 9, 12], 8)) # => False
