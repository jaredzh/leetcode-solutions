class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hi, lo = nums.index(max(nums)), nums.index(min(nums))
        return min(max(hi,lo)+1, n-min(hi,lo), min(hi, lo) + (n-max(hi, lo)+1))