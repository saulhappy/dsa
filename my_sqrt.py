"""
source: https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

"""
import math

def my_sqrt(num):
    return math.trunc(math.sqrt(num))

print(my_sqrt(4)) # => 2
print(my_sqrt(8)) # => 2
