from typing import List


class Solution:
    # более хитрое решение за 1 проход
    # из двух половинок смотрим, какая из них нормальная
    # затем сравниваем ископое число с границами нормальной половинки,
    # если ископое число в этой половинке, продолжаем посик в этой половине, иначе ищем в другой половине
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    # ищем начало последовательности до перевората
    # затем ищем отдельно в каждой половинке отдельно
    # если в одной из половинок нашлось, значит все хорошо, иначе элемента нет

    def search_1(self, nums: List[int], target: int) -> int:
        first = self.get_first_index(nums)
        print(first)
        res1 = self.half_search(nums, target, 0, first - 1)
        if res1 != -1:
            return res1
        res2 = self.half_search(nums, target, first, len(nums) - 1)
        if res2 != -1:
            return res2
        return -1

    def half_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        l = left
        r = right
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def get_first_index(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return l
