class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        def NChooseK(n, k):
            return factorial(n)/(factorial(k)*factorial(n-k))
        
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = dp[i-1]*NChooseK(i*2, 2)
            dp[i] %= (1e9+7)
        return int(dp[n])