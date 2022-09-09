# return second to last element of iterable
arr = [1, 2, 3, 4, 5]

def get_second_last(arr):
    for i in reversed(range(len(arr) - 1)):
        return arr[i]

print(get_second_last(arr))
