"""
source: https://leetcode.com/problems/jewels-and-stones/

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

"""

def num_jewels_in_stones(J, S):
    count = 0
    for char in J:
        count += S.count(char)
    return count


print(num_jewels_in_stones("aA", "aAAbbbb")) # => 3
