"""
SOURCE: https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

"""
wrong approach. need to create a pointer per ith element of array to count how many days go by until it gets a higher number
"""

# O(n^2) approach times out in Leetcode
# def daily_temperatures(temperatures):
#     n = len(temperatures)
#     answer = [0] * n
#     for day in range(n):
#         for future_day in range(day + 1, n):
#             if temperatures[future_day] > temperatures[day]:
#                 answer[day] = future_day - day
#                 break      
            
#     return answer

# Trying linear approach using a stack
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i, temp in reversed(list(enumerate(temperatures))):
        while stack and temp >= stack[0][0]:
            stack.pop(0)
        if stack and temp < stack[0][0]:
            result[i] = stack[0][1] - i
        stack.insert(0, [temp, i])

    return result
            


print(daily_temperatures([73,74,75,71,69,72,76,73]))  # => [1,1,4,2,1,1,0,0]

print(daily_temperatures([30,40,50,60]))  # => [1,1,1,0]

print(daily_temperatures([30,60,90]))  # => [1,1,0]
