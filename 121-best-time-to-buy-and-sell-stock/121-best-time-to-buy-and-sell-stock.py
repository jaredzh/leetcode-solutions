class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float("inf")
        prof = 0
        for p in prices:
            low = min(p, low)
            prof = max(prof, p-low)
        return prof