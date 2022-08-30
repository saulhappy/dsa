"""
given a target integer, and array of nums, return true/false if any combination of existing numbers in array sum to the target integer.
Seems like the Two Sum problem.

"""

def canSum(target_num, array):
    memo = {}

    for cur_num in array:
        if cur_num == target_num:
            return True
        if cur_num in memo.values():
            return True
        memo[cur_num] = target_num - cur_num
    return False


def canSumRec(target_num, array, memo = {}):
    if target_num in memo:
        return memo[target_num]
    if target_num == 0:
        return True
    if target_num < 0:
        return False

    for num in array:
        remainder = target_num - num
        if canSumRec(remainder, array, memo) == True:
            memo[target_num] = True
            return True

    memo[target_num] = False
    return False


# print(canSum(7, [5, 3, 4, 7])) # => True
# print(canSumRec(7, [5, 3, 4, 7])) # => True
# print(canSum(8, [2, 3, 5])) # => True
# print(canSumRec(8, [2, 3, 5])) # => True

# print(canSum(7, [2, 4])) # => False
# print(canSumRec(7, [2, 4])) # => False

# print(canSum(300, [7, 14])) # => False
# print(canSumRec(300, [7, 14])) # => False

