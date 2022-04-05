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
        
        while left <= right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1 if left else left