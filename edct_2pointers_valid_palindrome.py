"""
Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.
"""

def is_valid_palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True




# TESTS

print(is_valid_palindrome("baab")) # => True

print(is_valid_palindrome("abba")) # => True

print(is_valid_palindrome("abcba")) # => True

print(is_valid_palindrome("RACECAR")) # => True

print(is_valid_palindrome("saul")) # => False

print(is_valid_palindrome("RACEACAR")) # => False


"""
Time Complexity:
The time complexity is O(n) where n is the number of chars in the string. But this algo will run at O(n/2)
because two pointers traversing each other don't have to traverse entire string, and meet at the middle.

Space Complexity:
O(1) in order to store our two indexes.
"""