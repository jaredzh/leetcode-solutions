class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        l = [val for row in grid for val in row]
        dq = deque(l)
        for i in range(k):
            dq.appendleft(dq.pop())
        k = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = dq[k]
                k += 1
        return grid