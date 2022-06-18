class StockSpanner:

    def __init__(self):
        self.stack = []
        self.n = 0

    def next(self, price: int) -> int:
        self.n += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            result = self.n - self.stack[-1][1]
        else:
            result = self.n
        self.stack.append((price, self.n))
        return result

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
