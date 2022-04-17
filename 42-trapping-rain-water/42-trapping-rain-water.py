class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n, [0]*n
        
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        res = 0
        for i, h in enumerate(height):
            k = min(left[i], right[i]) - h
            res += k if k > 0 else 0
        return res