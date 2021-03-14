# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        need, res = False, ListNode(0)
        r = res
        while l1 or l2:
            if l1 and l2:
                tmp_num = l1.val + l2.val
            elif l1:
                tmp_num = l1.val
            else:
                tmp_num = l2.val
            if need:
                tmp_num += 1
            if tmp_num >= 10:
                tmp_num -= 10
                need = True
            else:
                need = False
            tmp_node = ListNode(tmp_num)
            r.next = tmp_node
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if need:
            tmp_node = ListNode(1)
            r.next = tmp_node
        return res.next
