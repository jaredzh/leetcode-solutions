# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ct = 1
        res = [-1]
        def solve(node):
            if not node:
                return
            solve(node.left)
            if self.ct == k:
                res[0] = node.val
            self.ct += 1
            solve(node.right)
        solve(root)
        return res[0]