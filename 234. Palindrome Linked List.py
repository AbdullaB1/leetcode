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
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middleNode(head)
        rev_middle = self.reverseList(middle)
        # обязательно проверяем именно по rev_middle, потому что это обрезанная и развернутая половина, 
        # а head в некотры случаях длинней (при четном количестве элементов, head на 1 элемент длиннее)
        while rev_middle:
            if rev_middle.val != head.val:
                return False
            head = head.next
            rev_middle = rev_middle.next
        
        return True
