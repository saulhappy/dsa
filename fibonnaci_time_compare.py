""" return nth number of fibonnaci sequence """
import time
fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,9227465, 14930352, 24157817, 39088169]

n = 38

# normal recursive:
def fibonnaci_rec(n):

    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci_rec(n - 1) + fibonnaci_rec(n - 2)

# normal recursive + memo:
def fibonnaci_rec_memo(n, memo = {}):
    if n in memo.keys(): return memo[n]
    if n <= 0: return None
    if n == 1 or n == 2: return 1
    else:
        memo[n] = fibonnaci_rec_memo(n - 1, memo) + fibonnaci_rec_memo(n - 2, memo)
    return memo[n]

# outputs

start = time.time()
print(f"the {n}th number of the fibonnaci sequence is {fib_sequence[n]}")
end = time.time()
print(f"look up of the {n}th number took {end - start} seconds")

start = time.time()
fibonnaci_rec(n)
end = time.time()

print(f"calculating the {n}th number with normal recursion took {end - start} seconds")

start = time.time()
fibonnaci_rec_memo(n)
end = time.time()

print(f"calculating the {n}th number with normal recursion with memo took {end - start} seconds")
