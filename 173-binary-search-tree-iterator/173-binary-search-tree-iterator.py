# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.l = []
        def f(n):
            if not n:
                return
            f(n.right)
            self.l.append(n.val)
            f(n.left)
        f(root)
        print(self.l)

    def next(self) -> int:
        return self.l.pop()

    def hasNext(self) -> bool:
        return self.l
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()