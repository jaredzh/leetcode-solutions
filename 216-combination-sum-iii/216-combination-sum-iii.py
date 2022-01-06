class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, k_in, num):
            if k_in > k:
                return
            if k_in == k and sum(path) == n:
                res.append(path)
            for i in range(num, 10):
                dfs(path+[i], k_in+1, i+1)
        dfs([], 0, 1)
        return res