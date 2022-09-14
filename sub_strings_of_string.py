"""
return all possible  substrings of a string

"""

def sub_strings_of_string(string):
    result = []

    for i in range(len(string)):
        for j in range(i, len(string)):
            result.append(string[i:j+1])
    return result

print(sub_strings_of_string("Saul"))
