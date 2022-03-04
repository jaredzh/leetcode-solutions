class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def numTrips(t):
            num = 0
            for v in time:
                num += t//v
            return num
    
        l = 0
        r = min(time)*totalTrips
        
        while l <= r:
            mid = (l+r)//2
            if numTrips(mid) < totalTrips:
                l = mid + 1
            else:
                r = mid - 1
        return l