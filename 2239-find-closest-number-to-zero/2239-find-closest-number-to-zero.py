class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res, k = -float("inf"), float("inf")
        for n in nums:
            if abs(n) < k:
                res = n
                k = abs(n)
            if abs(n) == k and n > res:
                res = n     
        return res