from typing import List


class Solution:
    # итерируемся с концов массива
    # каждый раз двигаем более низкий столбик
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            h = min(height[l], height[r])
            max_area = max(max_area, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

    # длинный и сложный вариант

    def maxArea_1(self, height: List[int]) -> int:
        max_idx, _ = max(enumerate(height), key=lambda x: x[1])
        left_br = []
        l = 0
        cur_max = 0
        while l < max_idx:
            if height[l] > cur_max:
                left_br.append((height[l], l))
                cur_max = height[l]
            l += 1
        left_br.append((height[max_idx], max_idx))

        right_br = []
        r = len(height) - 1
        cur_max = 0
        while r > max_idx:
            if height[r] > cur_max:
                right_br.append((height[r], r))
                cur_max = height[r]
            r -= 1
        right_br.append((height[max_idx], max_idx))

        l = 0
        r = 0
        max_area = 0
        while l < len(left_br) and r < len(right_br):
            max_area = max(
                max_area,
                min(left_br[l][0], right_br[r][0]) *
                (right_br[r][1] - left_br[l][1])
            )
            if left_br[l][0] < right_br[r][0]:
                l += 1
            else:
                r += 1
        return max_area
