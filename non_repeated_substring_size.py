"""
Given a string s, find the length of the longest substring that contains no repeated characters

"""

def non_repeated_substring_size(s):
    len_longest = 0
    all_substrings = get_all_substrings(s)
    
    for current_string in all_substrings:
        char_counts = {}
        for char in current_string:
            if char in char_counts.keys():
                char_counts[char] += 1
            else:
                char_counts[char] = 1      
        if sum(char_counts.values()) == len(char_counts.keys()):
            len_longest = max(len_longest, len(current_string))

    return len_longest

def get_all_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            result.append(s[i:j+1])
    return result


print(non_repeated_substring_size("nndNfdfdf")) #  => 4, because "ndNf" 
print(non_repeated_substring_size("aeiou")) #  => 5, because none repeat
print(non_repeated_substring_size("")) #  => 0
