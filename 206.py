class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head -> 1 -> 2 -> 3 ->4
# head -> 2 -> 1 -> 3 -> 4
# TODO


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, pre = head, None
        while p:
            pre, pre.next, p = p, pre, p.next
        return pre
