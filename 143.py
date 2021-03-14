class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 -> 2 -> 3
# 4 -> 5

# 1 -> 

class Solution:
    def reorderList(self, head: ListNode) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid, cur = slow.next, head
        slow.next = None
        tmp_mid_p, tmp_mid_pre = mid, None
        while tmp_mid_p:
            tmp_mid_pre, tmp_mid_pre.next, tmp_mid_p = tmp_mid_p, tmp_mid_pre, tmp_mid_p.next 
        mid = tmp_mid_pre
        while mid:
            tmp = mid.next
            mid.next = cur.next
            cur.next = mid
            mid = tmp
            cur = cur.next.next


            

