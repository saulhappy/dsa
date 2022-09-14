"""
source: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

"""

def array_strings_are_equal(word1, word2):
    return "".join(word1) == "".join(word2)


print(array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"])) # => True
print(array_strings_are_equal(["a", "cb"], ["ab", "c"])) # => False
print(array_strings_are_equal(["ab", "c"], ["a", "bc"])) # => True
