def is_palindrome(s):
    L = 0
    R = len(s) - 1

    while L < R:
        if s[L] == s[R]:
            L += 1
            R -= 1
        else:
            # at this point we'd if there's a single char to change left, then we know we can return false"
            new_string_in_test = s[L+1:R]
            if not new_string_in_test:
                return True
            if new_string_in_test != new_string_in_test[::-1]:
                return False
    return True

# not working. I suppose not getting the goal. 

# TEST CASES:
print(is_palindrome("RACEACAR")) # => True

print(is_palindrome("madame")) # => True

print(is_palindrome("abcdeca")) # => False


