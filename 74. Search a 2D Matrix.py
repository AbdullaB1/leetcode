from typing import List


class Solution:
    # локализируем поиск сначала до поиска в строки
    # затем пустим второй раз бинарный поиск уже по этой строке матрицы
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binsearch(matrix[mid], target)
            if matrix[mid][-1] <= target:
                l = mid + 1
            else:
                r = mid
        return self.binsearch(matrix[l], target)

    def binsearch(self, arr: list[int], target) -> bool:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    # через маппинг индекса в массиве и в матрице
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        n = len(matrix[0])
        r = len(matrix) * len(matrix[0]) - 1
        while l < r:
            m = (l + r) // 2
            if matrix[m // n][m % n] >= target:
                r = m
            else:
                l = m + 1
        return matrix[l // n][l % n] == target
