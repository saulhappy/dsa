"""
SOURCE: https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""

def first_unique_char(s):
    from collections import Counter
    s_counter = Counter(s)
    unique_chars = [char for char, value in s_counter.items() if value == 1]
    if len(unique_chars) == 0: return - 1

    for i in range(len(s)):
        if s[i] in unique_chars:
            return i
    return -1

print(first_unique_char("leetcode"))  # => 0
print(first_unique_char("loveleetcode"))  # => 2
print(first_unique_char("aabb"))  # => -1
