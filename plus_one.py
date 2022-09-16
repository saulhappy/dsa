"""
# source https://leetcode.com/problems/plus-one/
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Input: digits = [0]
Output: [1]
"""

"""
Algorithm: iterate in reverse. If that number is less than 10,
we can add 1 to that digit, and return immediately. Otherwise, it's a 10, 
we have to make it a 0, carry the one...but the loop will add one automatically. 
If at end of iteration, all have turned back to 0s, then we need to add a 1 at beginning. 

"""

def plus_one(digits):
    for i in reversed(range(len(digits))):
        digits[i] += 1
        if digits[i] != 10:
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits


print(plus_one([1,2,3])) # => [1,2,4]
print(plus_one([4,3,2,1])) # => [4,3,2,2]
print(plus_one([0])) # => [1]
