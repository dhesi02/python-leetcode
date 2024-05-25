class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result
        