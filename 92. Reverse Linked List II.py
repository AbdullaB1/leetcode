from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = ListNode()
        curr.next = head
        result = curr
        for i in range(left - 1):
            curr = curr.next
        # указатель на элемент, после которого нужно совершить разворот
        begin = curr
        for i in range(right - left + 2):
            curr = curr.next
        # концец списка, который нужно будет доцепить после переворота центральнйо части
        end = curr
        begin.next = self.reverseList(begin.next, right - left + 1, end)
        return result.next
        
    def reverseList(self, head: Optional[ListNode], lenght: int, end: Optional[ListNode]) -> Optional[ListNode]:
        """
        немного переделанная задача 206. Reverse Linked List
        https://leetcode.com/problems/reverse-linked-list/
        передаем конец, который нужно будет доцепить и длину переворота из head
        """
        prev = end
        curr = head
        while curr and lenght > 0:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
            lenght -= 1
        return prev
        

head = ListNode(3)
head.next = ListNode(5)
print(
    Solution().reverseBetween(head, 1, 2)
)
        