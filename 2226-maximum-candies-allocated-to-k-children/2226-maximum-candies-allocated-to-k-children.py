class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def is_valid(x: int) -> bool:
            if x == 0:
                return False
            count = 0
            for c in candies:
                count += (c//x)
            return count >= k
        
        left, right = 0, sum(candies)//k
        
        while left < right:
            mid = (left + right + 1) // 2
            if not is_valid(mid):
                right = mid - 1
            else:
                left = mid 
        return left