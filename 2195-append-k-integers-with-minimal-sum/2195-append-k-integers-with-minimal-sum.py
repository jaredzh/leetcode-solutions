class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def f(n):
            return n*(n+1)/2
        res = 0
        nums = sorted(list(set([0]+nums)))
        for i in range(len(nums)-1):
            if not k:
                break
            n1, n2 = nums[i], nums[i+1]-1
            to_add = n2-n1
            if not to_add:
                continue
            if to_add <= k:
                res += (f(n2)-f(n1))
                k -= to_add
            else:
                res += (f(n1+k)-f(n1))
                k = 0
        if k:
            res += (f(nums[-1]+k)-f(nums[-1]))
        return res