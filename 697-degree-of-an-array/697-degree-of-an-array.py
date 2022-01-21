class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        deg = 0
        res = len(nums)
        for i, v in enumerate(nums):
            d[v].append(i)
            deg = max(deg, len(d[v]))
        for k, v in d.items():
            if len(v) == deg:
                res = min(res, v[-1]-v[0]+1)
        return res