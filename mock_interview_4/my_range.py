class myPange:
    def __init__(self, first: int, second: int = None, step: int = 1):
        if not second:
            self.lower = 0
            self.upper = first
            self.step = step
        else:
            self.lower = first
            self.upper = second
            self.step = step
        self.curr = self.lower
        self.not_invalid = True
        if self.step < 0 and self.lower < self.upper:
            self.not_invalid = False
        if self.step > 0 and self.lower > self.upper:
            self.not_invalid = False

    def __iter__(self) -> None:
        return self

    def __next__(self):
        if self.curr < self.upper and self.not_invalid:
            res = self.curr
            self.curr += self.step
            return res
        else:
            raise StopIteration


class myRange:
    def __init__(self, begin=None, end=None, step=1) -> None:
        if not end:
            self.begin = 0
            self.end = begin
        else:
            self.begin = begin
            self.end = end
        self.step = step
        if abs(begin + step - end) >= abs(begin - end):
            self.begin = 1
            self.end = 1

    def __iter__(self) -> None:
        return self

    def __next__(self):
        if self.begin < self.end:
            self.begin += self.step
            return self.begin - self.step
        else:
            raise StopIteration


print([*myPange(5, 5)])
assert [*myPange(5, 5)] == []
assert [*myPange(5, 6)] == [5]
assert [*myPange(5, 10)] == [5, 6, 7, 8, 9]
assert [*myPange(5, -5)] == []
assert [*myPange(-2, 2)] == [-2, -1, 0, 1]
assert [*myPange(-2, 2, -2)] == []
assert [*myPange(-2, -2)] == []
print([*myPange(-2, 10)])


for i in myPange(5, 10):
    print(i)
