class Solution_1:
    def maxDistToClosest(self, seats: list[int]) -> int:
        isfistseq = True
        result = 0
        start = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if isfistseq:
                    result = i
                    isfistseq = False
                else:
                    result = max(result, (i - start) // 2)
                start = i
        result = max(result, len(seats) - start - 1)
        return result


class Solution:
    """немного другая реализация, но идея та же"""

    def maxDistToClosest(self, seats: list[int]) -> int:
        result = 0
        is_begin = True
        curr = 0
        for num in seats:
            if num == 0:
                curr += 1
                continue
            if is_begin:
                result = curr
                is_begin = False
            else:
                result = max(result, (curr - 1) // 2 + 1)
            curr = 0
        result = max(result, curr)
        return result
