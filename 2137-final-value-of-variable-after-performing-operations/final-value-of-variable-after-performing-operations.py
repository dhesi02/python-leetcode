class Solution(object):
    def finalValueAfterOperations(self, operations):
        ans=0
        for operate in operations:
            if operate == '--X' or operate == 'X--':
                ans-=1
            else:
                ans+=1
        return ans
        