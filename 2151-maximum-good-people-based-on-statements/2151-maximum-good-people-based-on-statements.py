class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        self.res = 0
        def is_valid(path):
            for i in range(n):
                if path[i]:
                    for j in range(n):
                        tmp = statements[i][j]
                        if tmp != 2 and tmp != path[j]:
                            return False
            return True
        
        def dfs(path, k):
            if len(path) == n:
                if is_valid(path):
                    self.res = max(self.res, k)
                return
            path.append(0)
            dfs(path, k)
            path[-1] = 1
            dfs(path, k+1)
            path.pop()
        
        dfs([], 0)
        return self.res