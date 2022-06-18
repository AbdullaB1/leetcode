# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        current = result

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return result.next


#         while head and head.val == val:
#             head = head.next

#         lastcorrect = head
#         current = head
#         while current:
#             if current.val == val:
#                 lastcorrect.next = current.next
#             else:
#                 lastcorrect = current
#             current = current.next
#         return head
