import re

def reverse_words(sentence):
    sentence = re.sub(' +',' ',sentence.strip())

    reversed_sentence = sentence[::-1]
    result = ""
    start = 0
    end = 0
    sentence_len = len(sentence)

    for i, char in enumerate(reversed_sentence):
        end += 1
        if char == " ":
            temp = reversed_sentence[start:end-1]
            temp = temp[::-1]
            result += temp + ' '
            start = i+1
        elif sentence_len - 1 == i:
            temp = reversed_sentence[start:end]
            temp = temp[::-1]
            result += temp

    return result


print(reverse_words("Hello Friend"))

print(reverse_words("Educative Answers")) # => # Answers Educative

print(reverse_words("Hurray 3 2 1")) # => # 1 2 3 Hurray

print(reverse_words("Reverse the words in a sentence")) # => # sentence a in words the Reverse

print(reverse_words("practice problems to improve your coding")) # => # coding your improve to problems practice
