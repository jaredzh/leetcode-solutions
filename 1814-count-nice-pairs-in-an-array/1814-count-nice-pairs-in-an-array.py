class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter()
        res = 0
        for a in nums:
            b = int(str(a)[::-1])
            res += d[a-b]
            d[a-b] += 1
        return res%(10**9 + 7)