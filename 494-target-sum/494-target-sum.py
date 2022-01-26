class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def deep(index, cur):
            if index == len(nums) and cur == target:
                return 1
            if index == len(nums):
                return 0
            return deep(index + 1, cur + nums[index]) + deep(index + 1, cur - nums[index])
    
        return deep(0, 0)