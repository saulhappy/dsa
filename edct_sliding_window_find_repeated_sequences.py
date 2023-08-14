def find_repeated_sequences(s, k):
    seen = []
    result = set()

    for i in range(len(s)):
        curr_string = s[i:k]
        if curr_string in seen:
            result.add(curr_string)
        else:
            seen.append(curr_string)
        k += 1

    return result


print(find_repeated_sequences(s="AGCTGAAAGCTTAGCTG", k=5)) # => ("AGCTG")

print(find_repeated_sequences(s="AGAGCTCCAGAGCTTG", k=6)) # => ("AGAGCT")

print(find_repeated_sequences(s="ATATATATATATATAT", k=6)) # => ("TATATA", "ATATAT")