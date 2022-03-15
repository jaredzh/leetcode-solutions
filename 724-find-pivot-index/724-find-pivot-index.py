class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)
        k = 0
        for i, n in enumerate(nums):
            left = k
            right = tot-k-n
            if left == right:
                return i
            k += n
        return -1
            