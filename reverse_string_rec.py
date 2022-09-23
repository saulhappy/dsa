def reverse_string_rec(string):
    if len(string) <= 1:
        return string

    return string[-1] + reverse_string_rec(string[:-1])


print(reverse_string_rec("saul")) # => "luas"
