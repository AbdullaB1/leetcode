from collections import deque


class RecentCounter:

    def __init__(self):
        self.k = 3000
        self.deque = deque()

    def ping(self, t: int) -> int:
        self.deque.append(t)
        while self.deque[0] < t - self.k:
            self.deque.popleft()
        return len(self.deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
