"""
source: https://leetcode.com/problems/rank-transform-of-an-array/

"""


def arr_rank_transform(arr):
    sortedArr = list(set(arr))
    sortedArr = sorted(sortedArr)
    sortedDict = {}
    result = []

    for index, num in enumerate(sortedArr, 1):
        sortedDict[num] = index

    for num in arr:
        result.append(sortedDict[num])

    return result


print(arr_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12, 12])) # -> [5, 3, 4, 2, 8, 6, 7, 1, 3, 3]
