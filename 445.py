# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_num, l2_num = 0, 0
        while l1:
            l1_num += l1.val
            l1 = l1.next
            l1_num *= 10
        l1_num //= 10
        while l2:
            l2_num += l2.val
            l2 = l2.next
            l2_num *= 10
        l2_num //= 10
        l1_num += l2_num
        if l1_num == 0:
            return ListNode(0)
        res = ListNode(None)
        while l1_num:
            tmp = ListNode(l1_num % 10)
            tmp.next = res.next
            res.next = tmp
            l1_num //= 10
        return res.next
