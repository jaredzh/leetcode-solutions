# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        def helper(node, l):
            if not node:
                return
            if not node.left and not node.right:
                nums.append("".join(l+[str(node.val)]))
            if node.left:
                helper(node.left, l+[str(node.val)])
            if node.right:
                helper(node.right, l+[str(node.val)])
        helper(root, [])
        res = 0
        for n in nums:
            res += int(n, 2)
        return res