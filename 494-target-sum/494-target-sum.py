class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        counts = Counter({0:1})
        for n in nums:
            d = Counter()
            for c in counts:
                d[c+n] += counts[c]
                d[c-n] += counts[c]
            counts = d
        return counts[target]