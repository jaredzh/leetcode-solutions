# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def solve(node):
            if not node:
                return [0, 0]
            
            l_sum, l_cnt = solve(node.left)
            r_sum, r_cnt = solve(node.right)
            
            k = (l_sum+r_sum+node.val) // (l_cnt+r_cnt+1)
            
            if node.val == k:
                res[0] += 1
            
            return [l_sum+r_sum+node.val, l_cnt+r_cnt+1]
        
        solve(root)
        return res[0]
            
            