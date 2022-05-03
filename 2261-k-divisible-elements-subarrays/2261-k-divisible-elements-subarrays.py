class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        n = len(nums)
        for i in range(n):
            l, ct = [], 0
            for j in range(i, n):
                if not nums[j] % p:
                    ct += 1
                l.append(nums[j])
                if ct <= k:
                    res.add(tuple(l))
        return len(res)