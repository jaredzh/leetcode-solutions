class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        s = set(nums)
        res = original
        while res in s:
            res *= 2
        return res