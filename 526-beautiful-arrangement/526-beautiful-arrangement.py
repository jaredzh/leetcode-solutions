class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        visited = [False] * (n+1)
        def dfs(path, pos):
            if pos > n:
                res[0] += 1
            for i in range(1, n+1):
                if not visited[i] and (not pos%i or not i%pos):
                    visited[i] = True
                    dfs(path+[pos], pos+1)
                    visited[i] = False
        dfs([], 1)
        return res[0]