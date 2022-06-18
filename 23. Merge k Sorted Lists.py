import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # а каждом шаге выбираем, из какого списка достать элемент через heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heap.append([l.val, i])
        heapq.heapify(heap)
        result = curr = ListNode(0)
        while heap:
            val, idx = heapq.heappop(heap)
            # можем использовать уже созданные ноды чтобы сэкономить память
            curr.next = lists[idx]
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(heap, [lists[idx].val, idx])
            curr = curr.next

        return result.next

    # мерджим попрано все списки, пока они все не объединятся в 1 большой
    # обычные массивы лучше так не мерждить,
    # так как в таком случае нужна доп память для хранения промежуточных результатов
    def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
