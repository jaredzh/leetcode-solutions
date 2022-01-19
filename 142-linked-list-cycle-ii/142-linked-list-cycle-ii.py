# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = defaultdict(int)
        i = 0
        while head and head not in d:
            d[head] = i
            i += 1
            head = head.next
        return head