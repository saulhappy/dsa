"""
write a function fib(n) that takes in a number as an argument. The function should return the 
nth number of the Fibonacci sequence. 

The 0th number of the sequence is 0.
The 1st number of the sequence is 1. 

To generate the next number of the sequence, we sum the previous two.

n:      0   1   2   3   4   5   6   7   8   9   ...
fib(n): 0   1   1   2   3   5   8   13  21  34  ...

"""

# normal recursive + memo:
def fibonnaci_rec_memo(n, memo = {}):
    if n in memo.keys(): return memo[n]
    if n <= 0: return 0
    if n == 1 or n == 2: return 1
    else:
        memo[n] = fibonnaci_rec_memo(n - 1, memo) + fibonnaci_rec_memo(n - 2, memo)
    return memo[n]
