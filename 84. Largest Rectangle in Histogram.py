from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                cur_h = heights[stack.pop()]
                cur_w = i - stack[-1] - 1
                max_area = max(max_area, cur_h * cur_w)
            stack.append(i)

        while stack[-1] != -1:
            cur_h = heights[stack.pop()]
            cur_w = len(heights) - stack[-1] - 1
            max_area = max(max_area, cur_h * cur_w)
        return max_area
