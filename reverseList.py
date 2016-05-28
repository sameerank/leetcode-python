# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recursiveReverse(head)

    def recursiveReverse(self, curr, prev=None):
        if curr == None:
            return prev
        next_node = curr.next
        curr.next = prev
        return self.recursiveReverse(next_node, curr)
