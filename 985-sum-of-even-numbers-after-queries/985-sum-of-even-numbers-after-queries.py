class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        k = 0
        for n in nums:
            if not n%2:
                k += n
        
        for q in queries:
            i, v = q[1], q[0]
            if not nums[i]%2 and not v%2:
                k+=v
            elif nums[i]%2 and v%2:
                k+=(nums[i]+v)
            elif not nums[i]%2 and v%2:
                k-=nums[i]
            nums[i] += v
            res.append(k)
        
        return res