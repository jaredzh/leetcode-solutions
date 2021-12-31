# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(r, curr_max, curr_min):
            if not r:
                return curr_max-curr_min
            
            curr_max = max(curr_max, r.val)
            curr_min = min(curr_min, r.val)
            
            l = helper(r.left, curr_max, curr_min)
            r = helper(r.right, curr_max, curr_min)
            
            return max(l,r)
        
        if not root:
            return 0
        
        return helper(root, root.val, root.val)