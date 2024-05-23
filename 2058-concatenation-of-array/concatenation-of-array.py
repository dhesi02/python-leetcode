class Solution(object):
    def getConcatenation(self, nums):
        nums.extend(list(nums))
        return nums
        