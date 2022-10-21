"""
source: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.

"""

def trim_mean(arr):
        arr.sort()
        
        five_percent_of_arr = len(arr) * 0.05
        sum_elements = 0
        n_elements = 0
        
        for i in range(int(five_percent_of_arr), (len(arr)) - int(five_percent_of_arr)):
            sum_elements += arr[i]
            n_elements += 1
            
        return sum_elements / n_elements



print(trim_mean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3])) # -> 2.0
print(trim_mean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0])) # -> 4.0
