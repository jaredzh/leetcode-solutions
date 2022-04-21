# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        def inorder(n):
            if not n:
                return
            inorder(n.left)
            l.append(n)
            inorder(n.right)
        inorder(root)
        fi, se = None, None
        for i in range(len(l)-1):
            n1, n2 = l[i], l[i+1]
            if n1.val > n2.val:
                if fi is None:
                    fi = i
                else:
                    se = i+1
        if not se:
            se = fi+1
        l[fi].val, l[se].val = l[se].val, l[fi].val