# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        ans = result
        addition = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            val = a + b + addition
            if val >= 10:
                addition = 1
                val -= 10
            else:
                addition = 0
            result.next = ListNode(val)
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if addition == 1:
            result.next = ListNode(1)
        return ans.next
