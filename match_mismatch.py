"""
Given two sentences, return an array that has the words that appear in one sentence and not the other and an array with the words in common. 

"""

def match_mismatch(string1, string2):
    sent1_arr = string1.split(" ")
    sent2_arr = string2.split(" ")
    match = []
    misMatch = []
    result = []

    for word in sent1_arr:
        if word in sent2_arr:
            match.append(word)

    for word in sent2_arr:
        if word in sent1_arr:
            match.append(word)

    for word in sent1_arr:
        if word not in sent2_arr:
            misMatch.append(word)

    for word in sent2_arr:
        if word not in sent1_arr:
            misMatch.append(word)

    result = [list(set(misMatch))]
    result += [list(set(match))]

    return result


print(match_mismatch('We are really pleased to meet you in our city', 'The city was hit by a really heavy storm')) # -> 
# (['The','We','a','are','by','heavy','hit','in','meet','our',
#     'pleased','storm','to','was','you'],
#  ['city', 'really'])

"""
ANTOHER ALGORITHM:

def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
    
    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

print(solution(sentence1, sentence2))

"""
