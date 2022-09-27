"""
source: https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

"""
Algo to try:
- Create result string
- Strip left and right the string
- Iterate the remove extra spaces
- Tterate through the input string:
    - create a word result string that stops when it sees an empty space, and inserts at position 0 to result string
- Return result string.

"""

def reverse_words(s):
    stripped_string_arr = list(s.strip())
    pre_result = ""
    result_arr = []
    
    for i in range(len(stripped_string_arr)):
        if stripped_string_arr[i] == " " and stripped_string_arr[i + 1] == " ": 
            i += 1
        else:
            pre_result += stripped_string_arr[i]
    
    current_word = ""
    for i in range(len(pre_result)):
        if pre_result[i] == " ": continue
        current_word += pre_result[i]
        try:
            if pre_result[i + 1] == " ":
                result_arr.insert(0, current_word)
                current_word = ""
        except IndexError:
            result_arr.insert(0, current_word)
            continue

    return " ".join(result_arr)


# TEST CASES

print(reverse_words("the sky is blue")) # => "blue is sky the"
print(reverse_words( "  hello world  ")) # => "world hello"
print(reverse_words("a good   example")) # => "example good a"
print(reverse_words("  Bob    Loves  Alice   ")) # => "Alice Loves Bob"
print(reverse_words("Alice does not even like bob")) # => "bob like even not does Alice"

