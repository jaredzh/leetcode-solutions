class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0]*n for i in range(m) ]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                k1, k2 = 0, 0
                if i > 0 and not obstacleGrid[i-1][j]:
                    k1 = dp[i-1][j]
                if j > 0 and not obstacleGrid[i][j-1]:
                    k2 = dp[i][j-1]
                dp[i][j] = k1+k2
        return dp[-1][-1] if not obstacleGrid[-1][-1] else 0