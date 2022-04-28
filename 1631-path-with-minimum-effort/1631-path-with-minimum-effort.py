class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        cost = [ [float("inf")] * n for _ in range(m) ]
        DIR = [0, 1, 0, -1, 0]
        pq = [(0, 0, 0)]
        
        while pq:
            val, r, c = heapq.heappop(pq)
            if cost[r][c] < val:
                continue
            if r == m-1 and c == n-1:
                return val
            for i in range(4):
                row, col = r+DIR[i], c+DIR[i+1]
                if 0 <= row < m and 0 <= col < n:
                    k = abs(heights[row][col] - heights[r][c])
                    new_cost = max(k, val)
                    if new_cost < cost[row][col]:
                        cost[row][col] = new_cost
                        heapq.heappush(pq, (new_cost, row, col))
            
            
            
    