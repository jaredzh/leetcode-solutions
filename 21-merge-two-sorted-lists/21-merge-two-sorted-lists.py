# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            v1, v2 = list1.val, list2.val
            if v1 >= v2:
                curr.next = ListNode(v2)
                list2 = list2.next
            else:
                curr.next = ListNode(v1)
                list1 = list1.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next