"""
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

"""
import math

def smallest_subarray_with_given_sum(arr, s):
    len_smallest_arr = math.inf 
    window_sum, window_start = 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            len_smallest_arr = min(len_smallest_arr, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
            if len_smallest_arr == math.inf: return 0
    return len_smallest_arr

# TEST CASES

print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)) # => 2. The smallest subarray with a sum greater than or equal to '7' is [5, 2].
print(smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7 )) # => 1. The smallest subarray with a sum greater than or equal to '7' is [8].
print(smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8 )) # => 3. Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
