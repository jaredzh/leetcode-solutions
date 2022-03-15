class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre = 0
        d = defaultdict(int)
        d[0] = 1
        res = 0
        for n in nums:
            pre += n
            res += d[pre-k]
            d[pre] += 1
        return res