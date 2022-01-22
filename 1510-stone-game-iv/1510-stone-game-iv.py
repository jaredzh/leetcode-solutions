class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False]*(n+1)
        
        for i in range(0, n+1):
            if dp[i]:
                continue
            for k in range(1, int(n**0.5)+1):
                idx = i+k**2
                if idx <= n:
                    dp[idx] = True
                else:
                    break
        return dp[n]