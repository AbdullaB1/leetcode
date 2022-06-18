from typing import List


class Solution:
    # чуть более лаконичное решение
    def formatRange(self, prev, curr):
        if prev == curr:
            return str(prev)
        return str(prev) + "->" + str(curr)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        prev = lower - 1
        for i, num in enumerate(nums):
            if num != prev + 1:
                ranges.append(self.formatRange(prev + 1, num - 1))
            prev = num
        if upper != prev:
            ranges.append(self.formatRange(prev + 1, upper))
        return ranges

    def findMissingRanges_1(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        prev = lower - 1
        for i, num in enumerate(nums):
            if num != prev + 1:
                if prev + 1 != num - 1:
                    ranges.append(str(prev + 1) + "->" + str(num - 1))
                else:
                    ranges.append(str(prev + 1))
            prev = num
        if upper != prev:
            if upper != prev + 1:
                ranges.append(str(prev + 1) + "->" + str(upper))
            else:
                ranges.append(str(upper))

        return ranges
