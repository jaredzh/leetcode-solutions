class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cand = None
        for n in nums:
            if not count:
                cand = n
            if cand == n:
                count += 1
            else:
                count -= 1
        return cand