class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = min(nums)
        max_n = max(nums)
        res = 0
        for n in nums:
            if n != min_n and n != max_n:
                res += 1
        return res