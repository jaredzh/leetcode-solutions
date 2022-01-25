class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def numBouquets(days):
            res = 0
            f = 0
            for d in bloomDay:
                if d > days:
                    f = 0
                else:
                    f += 1
                    res += f//k
                    f = f%k
            return res
        
        if len(bloomDay) < m*k:
            return -1
        left, right = min(bloomDay), max(bloomDay)
        
        while left <= right:
            mid = (left+right)//2
            if numBouquets(mid) < m:
                left = mid +1
            else:
                right = mid -1
        
        return left