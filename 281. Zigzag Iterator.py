from typing import List
from collections import deque


class ZigzagIterator_2:
    # плохое решение с большим количестов if-ов и граничными случаями
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.curr_idx = 0
        self.curr = self.v1
        self.prev_idx = 0
        self.prev = self.v2
        self.swap_after = True

    def next(self) -> int:
        if not self.hasNext:
            raise StopIteration
        if self.curr_idx < len(self.curr):
            elem = self.curr[self.curr_idx]
            self.curr_idx += 1
            if self.swap_after:
                self.curr_idx, self.prev_idx = self.prev_idx, self.curr_idx
                self.curr, self.prev = self.prev, self.curr
            return elem
        else:
            elem = self.prev[self.prev_idx]
            self.prev_idx += 1
            self.swap_after = False
            self.curr_idx, self.prev_idx = self.prev_idx, self.curr_idx
            self.curr, self.prev = self.prev, self.curr
            return elem

    def hasNext(self) -> bool:
        if self.curr_idx < len(self.curr) or self.prev_idx < len(self.prev):
            return True
        return False


class ZigzagIterator:
    # вариант через очередь
    # так же подойдет кольцевой список
    # если нельзя использовать deque.rotate(),
    # то можно deque.pop() -> deque.appendleft()
    def __init__(self, v1: List[int], v2: List[int]):
        self.q = deque()
        self.q_idx = deque()
        if len(v1) > 0:
            self.q.appendleft(v1)
            self.q_idx.appendleft(0)
        if len(v2) > 0:
            self.q.appendleft(v2)
            self.q_idx.appendleft(0)

    def next(self) -> int:
        elem = self.q[-1][self.q_idx[-1]]
        self.q_idx[-1] += 1
        if self.q_idx[-1] < len(self.q[-1]):
            self.q.rotate(1)
            self.q_idx.rotate(1)
        else:
            self.q.pop()
            self.q_idx.pop()
        return elem

    def hasNext(self) -> bool:
        return len(self.q) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())


# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1, 2, 3]
v2 = [5, 6, 7, 8, 9]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())
print(v)
