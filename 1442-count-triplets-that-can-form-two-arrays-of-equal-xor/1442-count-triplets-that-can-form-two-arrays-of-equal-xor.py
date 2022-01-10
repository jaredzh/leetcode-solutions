class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = 0
        for i in range(n):
            k = arr[i]
            for j in range(i+1, n):
                k = k ^ arr[j]
                if not k:
                    res += (j-i)
        return res