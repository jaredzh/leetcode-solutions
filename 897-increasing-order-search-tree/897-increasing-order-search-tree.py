# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = TreeNode()
        ret = self.res
        def solve(n):
            if not n:
                return
            solve(n.left)
            self.res.right = TreeNode(n.val)
            self.res = self.res.right
            solve(n.right)
        
        solve(root)
        return ret.right