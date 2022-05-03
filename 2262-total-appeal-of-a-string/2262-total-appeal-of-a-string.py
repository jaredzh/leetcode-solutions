class Solution:
    def appealSum(self, s: str) -> int:
        res, curr, d = 0, 0, defaultdict(lambda: -1)
        for i, val in enumerate(s):
            curr += (i - d[val])
            res += curr
            d[val] = i
        return res
        