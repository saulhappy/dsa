def vowel_count(word):
    return word.count("a") + word.count("e") + word.count("i") \
        + word.count("o") + word.count("u")


print(vowel_count("helicopter")) # -> 4
print(vowel_count("saul")) # -> 2
print(vowel_count("aaeeoo")) # -> 6
print(vowel_count("cdt")) # -> 0
