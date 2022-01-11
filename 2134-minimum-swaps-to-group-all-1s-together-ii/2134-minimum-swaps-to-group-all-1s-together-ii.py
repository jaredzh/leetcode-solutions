class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = nums.count(1)
        nums = nums+nums
        k, ones_wind = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i-ones]:
                k -= 1
            if nums[i]:
                k += 1
            ones_wind = max(ones_wind, k)
        return ones - ones_wind