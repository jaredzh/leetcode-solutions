class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(nums, tar, path):
            if tar < 0:
                return
            if tar == 0:
                res.append(path)
                return
            for i, v in enumerate(nums):
                dfs(nums[i:], tar-v, path+[v])
        dfs(candidates, target, [])
        return res