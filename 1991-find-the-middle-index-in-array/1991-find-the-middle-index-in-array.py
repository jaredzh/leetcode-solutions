class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right = [0]*n
        k=0
        for i in range(n-1, -1, -1):
            right[i]=k
            k += nums[i]
        
        k=0
        for i, v in enumerate(nums):
            if right[i]==k:
                return i
            k += v
        return -1