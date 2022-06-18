from collections import deque


class MyStack_1:
    # push - O(1)
    # pop and peak - O(n)
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q)
        for _ in range(n - 1):
            temp = self.q.popleft()
            self.q.append(temp)
        return self.q.popleft()

    def top(self) -> int:
        n = len(self.q)
        for _ in range(n - 1):
            temp = self.q.popleft()
            self.q.append(temp)
        res = self.q[0]
        temp = self.q.popleft()
        self.q.append(temp)
        return res

    def empty(self) -> bool:
        return len(self.q) == 0


class MyStack:
    # push - O(n)
    # pop and peak - O(1)
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q)
        for _ in range(n - 1):
            temp = self.q.popleft()
            self.q.append(temp)

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
