"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Write a function all_construct (target, wordBank) that accepts a target string and an array of strings. 

The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordbank' array. Each element of the 2D array should represent one combination that constructs the target. 

You may reuse elements of 'wordbank' as many times as needed. 

"""

# o(n^m) time, o(m) space (height of recursion tree). 
# Because ALL combinations must be returned, can't do better than exponential: 
# m levels of recursive tree x n possible combinations in word bank

def all_construct(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if target == '': return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word): # if the beginning of word is the 0th index of target,
            suffix = target[len(word):] # slice the word to get remainder after removing the amount of characters of word
            suffix_combos = all_construct(suffix, word_bank, memo)
            target_combos = insert_element(suffix_combos, word)
            result += target_combos
    
    memo[target] = result
    return result

def insert_element(arr, word):
    for element in arr:
        element.insert(0,word)
    return arr

# test cases

print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # => 
# [
#     ['purp', 'le'],
#     ['p', 'ur', 'p', 'le']
# ]

print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])) # =>
# [
#     ['ab', 'cd', 'ef'],
#     ['ab', 'c', 'def'],
#     ['abc', 'def'],
#     ['abcd', 'ef']
# ]

print(all_construct('hello', ['cat', 'dog', 'mouse'])) # => []

print(all_construct('', ['cat', 'dog', 'mouse'])) # => [[]] 

print(all_construct('aaaaaaaaaaaaaaaaaaz', ['aaa', 'a', 'aaaaaaa', 'aa', 'aaaaaaaaaaaaa'])) # => [] 
