# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5 # => [2.2, 2.8, 2.4, 3.6, 2.8] 


def find_averages_of_subarrays(K, arr):
  result = []

  for i in range(len(arr)-K + 1):
    current_sum = 0
    for j in range(K):
      current_sum += arr[i + j]
    result.append(current_sum / K)
  return result




print(find_averages_of_subarrays(K, arr))
