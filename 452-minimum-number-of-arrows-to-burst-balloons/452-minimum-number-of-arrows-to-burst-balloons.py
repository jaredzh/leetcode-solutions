class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[1])
        res, end = 0, -float("inf")
        
        for s, e in points:
            if s > end:
                end = e
                res += 1
        return res
            