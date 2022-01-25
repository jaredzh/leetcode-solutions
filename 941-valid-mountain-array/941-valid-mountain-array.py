class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        max_i = arr.index(max(arr))
        i = max_i-1
        while i >= 0:
            if not arr[i+1] > arr[i]:
                return False
            i -= 1
        i = max_i +1
        while i < n:
            if not arr[i-1] > arr[i]:
                return False
            i += 1
        return max_i != 0 and max_i != n-1