# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        walker = runner = head
        for _ in range(n):
            runner = runner.next
        if runner == None:
            return head.next
        while runner.next:
            runner = runner.next
            walker = walker.next
        walker.next = walker.next.next
        return head
