"""
SOURCE: https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

"""

def max_sub_array_of_size_k(arr, k):
    max_sum, window_sum, window_start = 0, 0, 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return max_sum

print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], k=3)) # => 9 Explanation: Subarray with maximum sum is [5, 1, 3].
print(max_sub_array_of_size_k([2, 3, 4, 1, 5], k=2 )) # => 7 Explanation: Subarray with maximum sum is [3, 4].
