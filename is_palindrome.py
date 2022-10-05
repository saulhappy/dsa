"""
source: https://leetcode.com/problems/palindrome-number/
"""

def is_palindrome(x):
    if x < 0:
        return False
    else:
        return x == int(str(x)[::-1])

print(is_palindrome(121)) # -> True
print(is_palindrome(-121)) # -> False
print(is_palindrome(88)) # -> True
print(is_palindrome(78)) # -> False
print(is_palindrome(3)) # -> True
