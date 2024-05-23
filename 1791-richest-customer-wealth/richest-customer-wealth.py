class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=0
        for customer in accounts:
            temp=0
            for value in customer:
                temp+=value
            ans=max(ans,temp)
        return ans
        