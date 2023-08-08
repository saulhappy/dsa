def square_sum_digits(num):
    string_num = str(num)
    total_sum = 0
    for num in string_num:
        total_sum += int(num) * int(num)
    return total_sum


def is_happy_number(n):
    slow = n
    fast = square_sum_digits(n)
    seen = []

    while True:
        if fast == 1 or slow == 1:
            return True
        
        if fast != 1 and fast != slow:
            slow = fast
            if slow not in seen:
                seen.append(slow)
            else:
                return False
            fast = square_sum_digits(square_sum_digits(fast))
            




print(is_happy_number(1)) # => True

print(is_happy_number(7)) # => True

print(is_happy_number(19)) # => True

print(is_happy_number(28)) # => True

print(is_happy_number(4)) # => False


# print(square_sum_digits(28)) # => 68
# print(square_sum_digits(68)) # => 100
# print(square_sum_digits(100)) # => 1
# print(square_sum_digits(1)) # => 1
# print(square_sum_digits(square_sum_digits(28))) # => 100




