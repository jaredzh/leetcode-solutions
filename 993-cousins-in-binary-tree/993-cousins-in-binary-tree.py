# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        bfs = [root]
        while bfs:
            next_level = []
            xy = set([x,y])
            for n in bfs:
                if n.left and n.right:
                    s = set([n.left.val, n.right.val])
                    if x in s and y in s:
                        return False
                if n.left:
                    if n.left.val == x:
                        xy.remove(x)
                    elif n.left.val == y:
                        xy.remove(y)
                    next_level.append(n.left)
                if n.right:
                    if n.right.val == x:
                        xy.remove(x)
                    elif n.right.val == y:
                        xy.remove(y)
                    next_level.append(n.right)
            if not xy:
                return True
            bfs = next_level
        return False