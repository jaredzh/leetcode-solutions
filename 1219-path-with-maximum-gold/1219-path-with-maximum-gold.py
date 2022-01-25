class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        
        def dfs(seen, i, j, gold):
            self.res = max(self.res, gold)
            seen[i][j] = True
            if i > 0 and grid[i-1][j] and not seen[i-1][j]:
                dfs(seen, i-1, j, gold+grid[i-1][j])
            if i < len(grid)-1 and grid[i+1][j] and not seen[i+1][j]:
                dfs(seen, i+1, j, gold+grid[i+1][j])
            if j > 0 and grid[i][j-1] and not seen[i][j-1]:
                dfs(seen, i, j-1, gold+grid[i][j-1])
            if j < len(grid[0])-1 and grid[i][j+1] and not seen[i][j+1]:
                dfs(seen, i, j+1, gold+grid[i][j+1])
            seen[i][j] = False
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen = [[False]*n for _ in range(m)]
                    dfs(seen, i, j, grid[i][j])
        return self.res