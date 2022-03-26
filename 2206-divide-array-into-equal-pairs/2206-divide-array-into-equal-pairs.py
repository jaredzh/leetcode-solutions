class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = Counter(nums)
        for _, v in d.items():
            if v%2:
                return False
        return True