class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def helper(k):
            ret = 0
            for pile in piles:
                ret += pile//k
                if pile%k:
                    ret += 1
            return ret
        
        low, high = 1, max(piles)
        
        while low <= high:
            mid = (low+high)//2
            
            if helper(mid) <= h:
                high = mid -1
            else:
                low = mid + 1
        return low
                
            