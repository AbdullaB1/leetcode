class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = []
        for inter in intervals:
            # проверить что result не пустой 
            # и что начало нового интервала пересекается с предидущим
            if result and inter[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], inter[1])
            else:
                result.append(inter)
        return result
