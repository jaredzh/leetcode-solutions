class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        memo = [[0]*(len(piles)+1) for _ in range(k+1)]
        
        @lru_cache(None)
        def dp(i, k):
            if i == len(piles) or k == 0:
                return 0
            #if memo[i][k] > 0:
                #return memo[i][k]
            res, curr = dp(i+1, k), 0
            for j in range(min(len(piles[i]), k)):
                curr += piles[i][j]
                res = max(res, curr + dp(i+1, k-j-1))
            return res
        return dp(0, k)