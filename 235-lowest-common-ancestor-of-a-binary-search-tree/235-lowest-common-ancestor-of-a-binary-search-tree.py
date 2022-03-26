# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lo, hi = min(p.val,q.val), max(p.val,q.val)
        if root.val > hi:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < lo:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        