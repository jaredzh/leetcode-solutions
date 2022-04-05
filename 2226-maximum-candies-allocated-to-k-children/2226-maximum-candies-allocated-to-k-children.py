class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def is_valid(x: int) -> bool:
            count = 0
            if x == 0:
                return False
            for c in candies:
                count += (c//x)
            return count >= k
        
        left, right = 0, sum(candies)//k + 1
        
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1 if left else left