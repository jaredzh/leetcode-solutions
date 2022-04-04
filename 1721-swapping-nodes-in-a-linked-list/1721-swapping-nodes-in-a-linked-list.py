# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second = None, None
        ptr = head
        
        i = 1
        while i < k:
            ptr = ptr.next
            i += 1
        first = ptr
        start = head
        while ptr.next:
            ptr = ptr.next
            start = start.next
        second = start
        
        first.val, second.val = second.val, first.val
        return head