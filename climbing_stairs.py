"""
source: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# Turns out this is the same problem as fibonnacci

def climb_stairs(n, memo={}):
    if n in memo.keys():
        return memo[n]

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    else:
        memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
        return memo[n] 

print(climb_stairs(2)) # => 2
print(climb_stairs(3)) # => 3
print(climb_stairs(5)) # => 8
