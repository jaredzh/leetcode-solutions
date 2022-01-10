# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf(root, l):
            if not root:
                return
            if root.left:
                leaf(root.left, l)
            if root.right:
                leaf(root.right, l)
            if not root.left and not root.right:
                l.append(root.val)
        l1 = []
        l2 = []
        leaf(root1, l1)
        leaf(root2, l2)
        return l1 == l2