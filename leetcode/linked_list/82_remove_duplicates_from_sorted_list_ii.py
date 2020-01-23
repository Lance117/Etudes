"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_duplicates(head):
    """
    I use a 'tail' that's always behind a 'ptr'. 'ptr' is used to compare the
    current node and next. If the values aren't equal, they move on.
    Otherwise, I save the value in a variable (x) and keep moving 'ptr' until
    it has a different value. Then the 'tail' hanging back can connect to 'ptr'.
    """
    dummy = tail = ListNode(None)
    dummy.next = ptr = head

    while ptr and ptr.next:
        if ptr.val != ptr.next.val:
            ptr, tail = ptr.next, tail.next
        else:
            x = ptr.val
            while ptr and ptr.val == x:
                ptr = ptr.next
            tail.next = ptr

        return dummy.next
