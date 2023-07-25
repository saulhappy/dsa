def find_sum_of_three(nums, target):
   sorted_nums = sorted(nums)
   L = 1
   R = len(sorted_nums) - 1

   for i in range(0, len(sorted_nums) - 2):
      L = i + 1
      R = len(sorted_nums) - 1

      while L < R:
         current_sum = sorted_nums[i] + sorted_nums[L] + sorted_nums[R]
         if current_sum == target:
            return True
         
         if current_sum < target:
            L += 1
         
         if current_sum > target:
            R -= 1
      
   return False


# TESTS

print(find_sum_of_three(nums=[2, 3, 1], target=6)) # => True

print(find_sum_of_three(nums=[1, -1, 1], target=2)) # => False

print(find_sum_of_three(nums=[1, 2, 4, 6, 8, 20], target=31)) # => False

print(find_sum_of_three(nums=[1, 3, 4, 6, 8, 20], target=31)) # => True
