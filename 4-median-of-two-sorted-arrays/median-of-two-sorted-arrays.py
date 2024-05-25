class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        return (merged[mid] + merged[mid - 1]) / 2.0 if n % 2 == 0 else merged[mid]