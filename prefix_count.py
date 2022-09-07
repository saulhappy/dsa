"""
source: https://leetcode.com/problems/counting-words-with-a-given-prefix/

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
.
"""

def prefix_count(words, pref):
    pref_count = 0

    for word in words:
        if word.startswith(pref): pref_count += 1
    return pref_count


# TEST CASES
print(prefix_count(words = ["pay","attention","practice","attend"], pref = "at")) # ==> 2
print(prefix_count(words = ["leetcode","win","loops","success"], pref = "code")) # ==> 0

