# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy
        while head:
            nxt = head.next
            dupe = False
            if nxt:
                while nxt.val == head.val:
                    dupe = True
                    nxt = nxt.next
                    if not nxt:
                        break
            if not dupe:
                curr.next = ListNode(head.val)
                curr = curr.next
            head = nxt
        return dummy.next
