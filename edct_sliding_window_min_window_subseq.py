"""
Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.
A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.
If there is no substring in str1 that covers all characters in str2, return an empty string.
If there are multiple minimum-length substrings that meet the subsequence requirement, return the one with the left-most starting index.

"""

def min_window(str1, str2):
    positive_window_start = 0
    positive_window_end = 0
    iteration_end = 1
    curr_min_window = [0,0]

    for i in range(len(str1)):
        if str2 in str1[i:iteration_end]:
            positive_window_start = i
            positive_window_end = iteration_end

    return ""

print(min_window(str1="abbcb", str2="ac")) # => "abbc"
# print(min_window(str1="abcdebdde", str2="bde")) # => "bcde"
# print(min_window(str1="abcdebdde", str2="bdf")) # => ""
# print(min_window(str1="this is a test string", str2="tis")) # => "this"
# print(min_window(str1="asbfgedasfbdaaf", str2="bfd")) # => "bfged"
# print(min_window(str1="Hello how are you", str2="ok")) # => ""
