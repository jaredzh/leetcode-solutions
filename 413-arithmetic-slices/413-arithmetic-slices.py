class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0
        dp = [0] * n
        if nums[2]-nums[1] == nums[1]-nums[0]:
            dp[2] = 1
        res = dp[2]
        for i in range(3, n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1]+1
            res += dp[i]
        return res