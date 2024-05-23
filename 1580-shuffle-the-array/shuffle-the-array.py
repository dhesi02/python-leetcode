class Solution(object):
    def shuffle(self, nums, n):
        ans=[]
        for i,j in zip(nums[:n],nums[n:]):
            ans+=[i,j]
        return ans