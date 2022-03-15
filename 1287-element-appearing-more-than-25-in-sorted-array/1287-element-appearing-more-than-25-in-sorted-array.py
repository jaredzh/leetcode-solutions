class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)//4
        for i in range(len(arr)-n):
            if arr[i]==arr[i+n]:
                return arr[i]
        