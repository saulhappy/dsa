"""
SOURCE: https://leetcode.com/problems/sort-characters-by-frequency/

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""

from collections import Counter

def frequency_sort(s):
    map = Counter(s).most_common()
    result = ""

    for i in range(len(map)):
        result += map[i][0] * map[i][1]
    return result



print(frequency_sort("tree"))  # => "eert"
print(frequency_sort("cccaaa"))  # => "aaaccc"
print(frequency_sort("Aabb"))  # => "bbAa"
