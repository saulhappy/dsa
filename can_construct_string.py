"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Write a function can_construct(target, wordBank) that accepts a target string and an array of strings. 
The function should return a boolean indicating whether or not the 
'target'can be constructed by concatenating elements of the 'wordbank' array. 
You may reuse elemnts of 'wordbank' as many times as needed. 

"""

# test cases

target0 = 'abcdef'
wordbank0 = ['ab', 'abc', 'cd', 'def', 'abcd']
# result0 => true

target1 = 'skateboard'
wordbank1 = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
# result1 => false

target2 = ''
wordbank2 = ['cat', 'dog', 'mouse']
# result2 => true

target3 = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
wordbank3 = ['ee', 'eeee', 'eeeeeee', 'eeeeeeeeeee', 'eeeeeeerrt']
# result3 => false

# BRUTE FORCE:
# M = len of target
# N = len of word bank
# time : O(N^M * M)
# space: O(M^2)

def can_construct(target, word_bank):
    if target == '': return True

    for word in word_bank:
        if target.startswith(word): # if the beginning of word is the 0th index of target,
            suffix = target[len(word):] # slice the word to get remainder after removing the amount of characters of word
            if can_construct(suffix, word_bank): return True
    return False

# MEMOIZED:
# M = len of target
# N = len of word bank
# time : O(N * M^2)
# space: O(M^2)

def can_construct_memo(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if target == '': return True

    for word in word_bank:
        if target.find(word) == 0: # if the beginning of word is the 0th index of target,
            suffix = target[len(word):] # slice the word to get remainder after removing the amount of characters of word
            if can_construct_memo(suffix, word_bank, memo): 
                memo[target] = True
                return True
    memo[target] = False
    return False

# print(can_construct(target0, wordbank0))
# print(can_construct(target1, wordbank1))
# print(can_construct(target2, wordbank2))
# print(can_construct(target3, wordbank3))

print(can_construct_memo(target0, wordbank0))
print(can_construct_memo(target1, wordbank1))
print(can_construct_memo(target2, wordbank2))
print(can_construct_memo(target3, wordbank3))

