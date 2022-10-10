"""
source: https://leetcode.com/problems/richest-customer-wealth/

"""


def max_wealth(accounts):
    return max(sum(account) for account in accounts) 


print(max_wealth([[1,2,3],[3,2,1]])) # -> 6
print(max_wealth([[1,5],[7,3],[3,5]])) # -> 10
print(max_wealth([[2,8,7],[7,1,3],[1,9,5]])) # -> 17
