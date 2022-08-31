"""
Given an array of characters return a string that counts the number of each consecutive letter.

Example: [“a”, “b”, “b”, “a”] should return “a1b2a1”
"""


def count_consecutive_element(arr):
    result = ""
    count = 1

    for i in range(len(arr)):
        try:
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                result += f"{arr[i]}{count}"
                count = 1
        except IndexError:
            result += f"{arr[i]}{count}"
            break
    return result


print(count_consecutive_element(["a", "b", "b", "a"]))  # => "a1b2a1"
print(count_consecutive_element(["a", "b", "b", "b", "a", "a"]))  # => "a1b3a2"
print(count_consecutive_element(["c", "c", "c", "c"]))  # => "c4"
print(count_consecutive_element(["a", "b", "b", "b", "a", "a", "c"]))  # => "a1b3a2c1"
