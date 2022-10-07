"""
For a giving string, get all the substring combinations.

"""

def get_all_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            result.append(s[i:j+1])
    return result


print(get_all_substrings("abc")) # -> ['a', 'ab', 'abc', 'b', 'bc', 'c']
