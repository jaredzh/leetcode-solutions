class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_p = float("inf")
        max_prof = 0
        
        for n in nums:
            min_p = min(min_p, n)
            max_prof = max(max_prof, n-min_p)
        
        return -1 if not max_prof else max_prof