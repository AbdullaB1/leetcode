# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        merged = ListNode(0)
        result = merged

        while first and second:
            if first.val < second.val:
                merged.next = first
                first = first.next
            else:
                merged.next = second
                second = second.next

            merged = merged.next

        while first:
            merged.next = first
            first = first.next
            merged = merged.next

        while second:
            merged.next = second
            second = second.next
            merged = merged.next

        return result.next
