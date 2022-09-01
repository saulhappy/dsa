"""
SOURCE: https://leetcode.com/problems/count-vowel-substrings-of-a-string/

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.


"""


def is_only_vowel_substring(string):
    vowels = "aeiou"
    test1 =  "a" in string and "e" in string and "i" in string and "o" in string and "u" in string
    test2 = True 

    for char in string:
        if char not in vowels: 
            test2 = False
            break
    return test1 and test2

def make_substrings(string):
    result = []

    for i in range(len(string)):
        for j in range(i, len(string)):
            result.append(string[i:j+1])
    return result

def count_vowel_substrings(word):
    substrings = make_substrings(word)
    count = 0
    for string in substrings:
        if is_only_vowel_substring(string): count += 1
    return count
    

# # TEST CASES
print(count_vowel_substrings(word = "aeiouu")) # => 2
print(count_vowel_substrings(word = "unicornarihan")) # => 0
print(count_vowel_substrings(word = "cuaieuouac")) # => 7
print(count_vowel_substrings(word = "bbaeixoubb")) # => 0
