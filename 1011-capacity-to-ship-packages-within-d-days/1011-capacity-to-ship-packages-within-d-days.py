class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        
        def days_to_ship(capacity):
            ret, i, k = 0, 0, 0
            while i < len(weights):
                k += weights[i]
                if k > capacity:
                    k = weights[i]
                    ret += 1
                i += 1
            return ret
        
        while left <= right:
            mid = (left+right)//2
            if days_to_ship(mid) < days:
                right = mid-1
            else:
                left = mid+1
        return left