# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # slow = head
        # fast = head
        # while slow and fast:
        #     if not fast.next:
        #         return slow
        #     fast = fast.next
        #     slow = slow.next
        #     if not fast.next:
        #         return slow
        #     fast = fast.next
        # return slow

        # count = 0
        # current = head
        # while current:
        #     count += 1
        #     current = current.next
        # result = head
        # for _ in range(count // 2):
        #     result = result.next
        # return result
