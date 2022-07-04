class Solution:
    def trap(self, height: list[int]) -> int:
        max_index, _ = max(enumerate(height), key=lambda x: x[1])
        result = 0
        prev_max = height[0]
        for i in range(1, max_index):
            if height[i] < prev_max:
                result += prev_max - height[i]
            prev_max = max(prev_max, height[i])
        prev_max = height[-1]
        for i in range(len(height) - 1, max_index, -1):
            if height[i] < prev_max:
                result += prev_max - height[i]
            prev_max = max(prev_max, height[i])
        return result
