# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(root, path):
            if not root:
                return
            inorder(root.left, path)
            path.append(root.val)
            inorder(root.right, path)
            return path
        l1, l2 = [], []
        inorder(root1, l1)
        inorder(root2, l2)
        return heapq.merge(l1, l2)