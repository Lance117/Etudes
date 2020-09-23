# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(117)
        sentinel.next = head
        lion = gazelle = sentinel
        for i in range(n + 1):
            gazelle = gazelle.next
        while gazelle:
            lion, gazelle = lion.next, gazelle.next
        lion.next = lion.next.next
        return sentinel.next
