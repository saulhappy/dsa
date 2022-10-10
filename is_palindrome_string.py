"""
Given a string, return true if the string is a palindrome or false if it is not.
Palindromes are strings that form the same word if it is reversed.
*Do* include spaces and punctuation in determining if the string is a palindrome.

"""


def is_palindrome_string(string):
    return string[::-1] == string

print(is_palindrome_string(("racecar"))) # -> True
print(is_palindrome_string(("abba"))) # -> True
print(is_palindrome_string(("saul"))) # -> False
print(is_palindrome_string(("radar"))) # -> True
