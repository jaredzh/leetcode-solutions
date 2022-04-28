class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import numpy
        left, right = 0, numpy.amax(heights) - numpy.amin(heights)
        end = [len(heights), len(heights[0])]
        def dfs(k, visited, i, j) -> bool:
            if i == end[0]-1 and j == end[1]-1:
                return True
            visited[i][j] = True
            cur_h = heights[i][j]
            if i > 0 and not visited[i-1][j] and abs(cur_h-heights[i-1][j]) <= k:
                if dfs(k, visited, i-1, j):
                    return True
            if i < end[0]-1 and not visited[i+1][j] and abs(cur_h-heights[i+1][j]) <= k:
                if dfs(k, visited, i+1, j):
                    return True
            if j > 0 and not visited[i][j-1] and abs(cur_h-heights[i][j-1]) <= k:
                if dfs(k, visited, i, j-1):
                    return True
            if j < end[1]-1 and not visited[i][j+1] and abs(cur_h-heights[i][j+1]) <= k:
                if dfs(k, visited, i, j+1):
                    return True
            return False
        
        while left <= right:
            mid = (left + right) // 2
            vis = [ [False]*end[1] for _ in range(end[0]) ]
            if not dfs(mid, vis, 0, 0):
                left = mid + 1
            else:
                right = mid - 1
        return left
            
    