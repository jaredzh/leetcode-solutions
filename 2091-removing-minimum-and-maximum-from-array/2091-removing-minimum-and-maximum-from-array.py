class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hi, lo = nums.index(max(nums)), nums.index(min(nums))
        k1, k2 = 1e9, 1e9
        k1 = max(hi,lo)+1
        k2 = n-min(hi,lo)
        return min(k1, k2, min(hi, lo) + (n-max(hi, lo)+1))