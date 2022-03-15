# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = defaultdict(TreeNode)
        parents = set()
        childs = set()
        for parent, child, isLeft in descriptions:
            parents.add(parent)
            childs.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if isLeft:
                nodes[parent].left =nodes[child]
            else:
                nodes[parent].right = nodes[child]
        return nodes[(parents-childs).pop()]
        
        