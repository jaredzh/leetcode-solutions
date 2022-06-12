class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        @lru_cache
        def dp(i, j):
            if i >= len(grid) - 1:
                return grid[i][j]
            
            m_cost = float("inf")
            cost = 0
            for k in range(len(grid[0])):
                cost = grid[i][j] + moveCost[grid[i][j]][k] + dp(i+1, k)
                m_cost = min(cost, m_cost)
            
            return m_cost
        
        res = float("inf")
        for j in range(len(grid[0])):
            res = min(res, dp(0, j))
        return res