"""
source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Given the array candies and the integer extraCandies, where candies[i] represents the number 
of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids 
such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.

"""

def kids_with_candies(candies, extraCandies):
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return result

print(kids_with_candies([2, 3, 5, 1, 3], 3)) # -> [true,true,true,false,true]
