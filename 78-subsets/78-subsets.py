class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, n):
            res.append(path)
            if not n:
                return
            for i, v in enumerate(n):
                dfs(path+[v], n[i+1:])
        dfs([], nums)
        return res