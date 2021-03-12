class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        cur = head
        fast = head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            cur = cur.next
            if fast == cur:
                break
        cur = head
        while cur != fast:
            cur = cur.next
            fast = fast.next
        return cur
