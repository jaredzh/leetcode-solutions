# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        def helper(curr, end):
            prev = None
            tmp = curr
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return [tmp, prev]
        start = None
        cur = None
        if left == 1:
            cur = head
        else:
            start = head
            while left > 2:
                start = start.next
                left -= 1    
            cur = start.next
        end = head
        while right:
            end = end.next
            right -= 1
        ret = helper(cur, end)
        if ret[0]:
            ret[0].next = end
        if not start:
            return ret[1]
        else:
             start.next = ret[1]
        return head
        