class HitCounter():
    def __init__(self) -> None:
        self.K = 10
        self.times = [0] * self.K
        self.hits = [0] * self.K

    def hit(self, timestamp: int) -> None:
        idx = timestamp % self.K
        if self.times[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.times[idx] = timestamp
            self.hits[idx] = 1

    def get_hits_count(self, timestamp: int) -> int:
        hits_count = 0
        for i in range(self.K):
            if timestamp - self.times[i] < self.K:
                hits_count += self.hits[i]
        return hits_count


counter = HitCounter()
while True:
    t = int(input())
    counter.hit(t)
    print("counts is", counter.get_hits_count(t))
    print(counter.times)
    print(counter.hits)
