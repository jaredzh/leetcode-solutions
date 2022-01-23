class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = 0
        k = 0
        for n in nums:
            if n == target:
                k += 1
            elif n < target:
                less += 1
        if not k:
            return []
        return [i for i in range(less, less+k)]