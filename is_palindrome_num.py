"""
source: https://leetcode.com/problems/palindrome-number/
"""

def is_palindrome_num(x):
    if x < 0:
        return False
    else:
        return x == int(str(x)[::-1])

print(is_palindrome_num(121)) # -> True
print(is_palindrome_num(-121)) # -> False
print(is_palindrome_num(88)) # -> True
print(is_palindrome_num(78)) # -> False
print(is_palindrome_num(3)) # -> True
