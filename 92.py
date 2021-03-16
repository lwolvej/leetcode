class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy.next


def print_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head, h_1, h_2, h_3, h_4 = ListNode(1), ListNode(
        2), ListNode(3), ListNode(4), ListNode(5)
    head.next, h_1.next, h_2.next, h_3.next, h_4.next = h_1, h_2, h_3, h_4, None
    s = Solution()
    res = s.reverseBetween(head, 2, 4)
    print_list(res)
