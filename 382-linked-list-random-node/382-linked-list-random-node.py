# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.nodes[random.randrange(0, len(self.nodes))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()