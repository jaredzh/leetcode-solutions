# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        d = {0:dummy}
        pre = 0
        while head:
            pre += head.val
            d[pre] = head
            head = head.next
        
        head = dummy
        pre = 0
        while head:
            pre += head.val
            head.next = d[pre].next
            head = head.next
        return dummy.next