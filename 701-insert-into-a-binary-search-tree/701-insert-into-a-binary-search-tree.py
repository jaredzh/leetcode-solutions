# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def helper(node, val):
            if not node.left and node.val > val:
                node.left = TreeNode(val)
                return
            if not node.right and node.val < val:
                node.right = TreeNode(val)
                return
            if node.val > val:
                helper(node.left, val)
            else:
                helper(node.right, val)
        
        if not root:
            return TreeNode(val)
        helper(root, val)
        return root