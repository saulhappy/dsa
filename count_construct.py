"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Write a function count_construct(target, wordBank) that accepts a target string and an array of strings. 
The function should return the number of ways that the 
'target'can be constructed by concatenating elements of the 'wordbank' array. 
You may reuse elemnts of 'wordbank' as many times as needed. 

"""

def count_construct(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if target == '': return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word): 
            suffix = target[len(word):] # slice the word to get remainder after removing the amount of characters of word
            numWays = count_construct(suffix, word_bank, memo)
            total_count += numWays
    memo[target] = total_count
    return total_count




# test cases
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # => 1
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # => 2
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # => 0
print(count_construct('', ['cat', 'dog', 'mouse'])) # => 1
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # => 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['ee', 'eeee', 'eeeeeee', 'eeeeeeeeeee', 'eeeeeeerrt'])) # => 0
