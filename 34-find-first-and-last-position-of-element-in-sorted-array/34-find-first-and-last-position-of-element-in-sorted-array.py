class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, n-1
        
        if not n:
            return [-1, -1]
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        
        left2, right2 = 0, n-1
        while left2 <= right2:
            mid = (left2+right2) // 2
            if nums[mid] > target:
                right2 = mid - 1
            else:
                left2 = mid + 1
 
        if left >= n or nums[left] != target:
            return [-1, -1]
        
        return [left, right2]