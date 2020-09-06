# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = tail = ListNode(0)
        sentinel.next = tail.next = head
        for _ in range(1, m):
            tail = tail.next
        trav = tail.next
        for _ in range(n - m):
            next = trav.next
            trav.next = next.next
            next.next = tail.next
            tail.next = next
        return sentinel.next
