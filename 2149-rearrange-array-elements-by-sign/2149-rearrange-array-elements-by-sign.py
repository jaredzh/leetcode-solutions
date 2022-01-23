class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg = []
        pos = []
        for n in nums:
            if n < 0:
                neg += [n]
            else:
                pos += [n]
        res = []
        for n, p in zip(neg, pos):
            res += [p, n]
        return res