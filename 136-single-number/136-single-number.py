class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [k for k, v in Counter(nums).items() if v==1][0]