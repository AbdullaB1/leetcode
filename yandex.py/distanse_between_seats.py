class Solution:
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
