"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""

def max_length_between_equal_chars(s):
    firstSeen = {}
    maxDist = -1
    
    for index, char in enumerate(s):
        if char not in firstSeen:
            firstSeen[char] = index
        else:
            maxDist = max(index - firstSeen[char], maxDist)

    if maxDist == -1:
        return maxDist
    else:
        return maxDist - 1


print(max_length_between_equal_chars('aa')) # -> 0
print(max_length_between_equal_chars('abca')) # -> 2
print(max_length_between_equal_chars('cbzxy')) # -> -1
