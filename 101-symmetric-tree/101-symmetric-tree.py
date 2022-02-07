# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(left, right):
            if not left and not right:
                return True
            if (left and not right) or (not left and right):
                return False
            return left.val==right.val and f(left.right, right.left) and f(left.left, right.right)
        
        return f(root.left, root.right)