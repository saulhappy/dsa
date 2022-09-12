"""
write a function fib(n) that takes in a number as an argument. The function should return the 
nth number of the Fibonacci sequence. 

The 0th number of the sequence is 0.
The 1st number of the sequence is 1. 

To generate the next number of the sequence, we sum the previous two.

n:      0   1   2   3   4   5   6   7   8   9   ...
fib(n): 0   1   1   2   3   5   8   13  21  34  ...

"""

def fib_tab(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, len(table)):
        table[i] = table[i-1] + table[i-2]
    return table[n]


print(fib_tab(6))   # => 8
print(fib_tab(7))   # => 13
print(fib_tab(8))   # => 21
print(fib_tab(50))  # => 12586269025
