class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, seen, n):
            res.append(path)
            if not n:
                return
            for i, v in enumerate(n):
                if v in seen:
                    continue
                seen.add(v)
                dfs(path+[v], seen, n[i+1:])
                seen.remove(v)
        dfs([], set(), nums)
        return res