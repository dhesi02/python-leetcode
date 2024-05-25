class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        check=max(candies)
        print(check)
        ans=[]
        for i in range(len(candies)):
            ck=candies[i]+extraCandies
            ans.append(ck>=check)
        return ans
        