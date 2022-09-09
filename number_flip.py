"""
You are given an integer n consisting of digits 1, 2, and 3 and you can flip one digit to a 3. Return the maximum number you can make.

Example 1
Input
n = 123
Output
323
Explanation
We flip 1 to 3

Example 2
Input
n = 333
Output
333
Explanation
Flipping doesn't help.
"""

def number_flip(n):
    new_num = str(n)
    result = ''

    for i in range(len(new_num)):
        if new_num[i] == '3':
            result += new_num[i]
        if new_num[i] != '3':
            result += '3' + new_num[i+1:len(new_num)]
            return int(result)
    return int(result)

print(number_flip(331)) # => 333
print(number_flip(321)) # => 331
print(number_flip(3222)) # => 3322
print(number_flip(123)) # => 323
print(number_flip(333)) # => 333
