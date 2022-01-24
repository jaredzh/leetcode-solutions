class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = Counter(nums)
        res = []
        for k, v in d.items():
            if v == 1 and k+1 not in d and k-1 not in d:
                res.append(k)
        return res