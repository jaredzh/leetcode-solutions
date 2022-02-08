class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odd, even, res = 0, 0, 0
        for n in arr:
            if not n%2:
                even += 1
            else:
                odd, even = even, odd
                odd += 1
            res += odd
        return int(res%(1e9+7))