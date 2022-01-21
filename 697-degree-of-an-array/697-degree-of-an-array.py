class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = Counter(nums)
        max_n = 0
        freq = 0
        for k, v in d.items():
            if v > freq:
                freq = v
                max_n = k
        cands = [x for x, v in d.items() if v == freq]
        res = len(nums)
        nums_reversed = nums[::-1]
        for c in cands:
            res = min(res, (len(nums)-1-nums_reversed.index(c))-nums.index(c)+1)
        return res
        