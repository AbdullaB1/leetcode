from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = curr_left = ListNode()
        right = curr_right = ListNode()
        curr = head
        while curr:
            temp = curr.next
            if curr.val < x:
                curr_left.next = curr
                curr_left = curr_left.next
            else:
                curr_right.next = curr
                curr_right = curr_right.next
            curr = temp
        # обязательно не забыть завершить последний элемент из правого списка
        # иначе в списке могут появитсья циклы
        curr_right.next = None
        curr_left.next = right.next
        return left.next
