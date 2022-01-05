class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(n_in, path, k_in):
            if not k_in:
                res.append(path)
                return
            for i in range(n_in, n+1):
                dfs(i+1, path+[i], k_in-1)
        dfs(1, [], k)
        return res