def vowel_count(word):
    return word.count("a") + word.count("e") + word.count("i") \
        + word.count("o") + word.count("u")


# print(vowel_count("helicopter")) # -> 4
# print(vowel_count("saul")) # -> 2
# print(vowel_count("aaeeoo")) # -> 6
# print(vowel_count("cdt")) # -> 0


test1 = vowel_count("helicopter")
expected1 = 4
if test1 == expected1:
    print("Pass")
else:
    print(f"Fail - expected: {expected1}, got: {test1}")

test2 = vowel_count("Saul")
expected2 = 2
if test1 == expected1:
    print("Pass")
else:
    print(f"Fail - expected: {expected1}, got: {test1}")

test3 = vowel_count("aaeeoo")
expected3 = 6
if test1 == expected1:
    print("Pass")
else:
    print(f"Fail - expected: {expected1}, got: {test1}")

test4 = vowel_count("cdt")
expected4 = 0
if test1 == expected1:
    print("Pass")
else:
    print(f"Fail - expected: {expected1}, got: {test1}")