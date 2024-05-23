class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i,j in zip(nums[:n],nums[n:]):
            ans+=[i,j]
        return ans