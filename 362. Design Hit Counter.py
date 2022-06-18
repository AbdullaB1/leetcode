from collections import deque


class SimpleHitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


class HitCounter:
    def __init__(self):
        self.k = 300
        self.hits = [0] * self.k
        self.last_hits = [0] * self.k

    def hit(self, timestamp: int) -> None:
        idx = timestamp % self.k
        if self.last_hits[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.hits[idx] = 1
            self.last_hits[idx] = timestamp

    def getHits(self, timestamp: int) -> int:
        hits_count = 0
        for i in range(self.k):
            if self.last_hits[i] > timestamp - 300:
                hits_count += self.hits[i]
        return hits_count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
