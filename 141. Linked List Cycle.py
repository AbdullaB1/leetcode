# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        while first is not None and second is not None:
            first = first.next
            second = second.next
            if second is None:
                return False
            second = second.next
            if id(second) == id(first):
                return True
        return False

        # node_set = set()
        # node_set.add(id(head))
        # while head is not None:
        #     head = head.next
        #     if id(head) in node_set:
        #         return True
        #     node_set.add(id(head))
        # return False
