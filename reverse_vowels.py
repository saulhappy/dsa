"""
source: https://leetcode.com/problems/reverse-vowels-of-a-string/
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

"""
def reverse_vowels(s):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    vowels_stack = []
    rev_str_arr = []

    for i in range(len(s)):
         if s[i] in vowels:
             vowels_stack.insert(0, s[i])
    
    for i in range(len(s)):
        if s[i] in vowels:
            rev_str_arr.append(vowels_stack.pop(0))
        else:
            rev_str_arr.append(s[i])
    
    return ''.join(rev_str_arr)

print(reverse_vowels("hello")) # => "holle"
print(reverse_vowels("leetcode")) # => "leotcede"
