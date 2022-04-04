# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second, ptr1 = None, None, head
        
        for _ in range(1, k):
            ptr1 = ptr1.next
            
        first, ptr2 = ptr1, head
        while ptr1.next:
            ptr1, ptr2 = ptr1.next, ptr2.next
            
        second = ptr2
        first.val, second.val = second.val, first.val
        return head