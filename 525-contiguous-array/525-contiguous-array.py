class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0:0}
        k = 0
        res = 0
        for i, n in enumerate(nums,1):
            if not n:
                k -= 1
            else:
                k += 1
            
            if k in d:
                res = max(res, i-d[k])
            else:
                d[k] = i
        return res