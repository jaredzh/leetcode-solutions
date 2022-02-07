class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        left = [a[:] for a in grid]
        up = [a[:] for a in grid]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        up[i][j] = 1+up[i-1][j]
                    if j:
                        left[i][j] = 1+left[i][j-1]
        for r in range(min(m,n), 0, -1):
            for i in range(m-r+1):
                for j in range(n-r+1):
                    k = min(up[i+r-1][j+r-1], left[i+r-1][j+r-1],
                            up[i+r-1][j], left[i][j+r-1])
                    if k >= r:
                        return r*r
        return 0
        