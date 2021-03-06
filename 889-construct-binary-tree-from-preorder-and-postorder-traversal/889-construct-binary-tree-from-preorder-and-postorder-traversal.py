# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not postorder:
            return None
        k = postorder.pop()
        root = TreeNode(k)
        preorder.pop(0)
        if not postorder or not preorder:
            return root
        next_root = postorder[-1]
        i = preorder.index(next_root)
        root.right = self.constructFromPrePost(preorder[i:], postorder)
        root.left = self.constructFromPrePost(preorder[:i], postorder)
        return root