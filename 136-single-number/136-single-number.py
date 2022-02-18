class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for n in nums:
            xor^=n
        return xor