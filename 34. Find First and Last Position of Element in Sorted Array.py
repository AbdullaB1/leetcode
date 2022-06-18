from typing import List


class Solution_2:
    # решение с использованием только правого поиска
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # вернет самый приближенный к (target - 1) индекс,
        # по которому мы сможет найти первого вхождение target
        left = self.right_search(nums, target - 1)
        if nums[left] == target:
            left -= 1
        right = self.right_search(nums, target)
        if nums[right] == target:
            return [left + 1, right] if left != right else [right, right]
        return [-1, -1]

    # эталонный правый поиск
    def right_search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return l


# решение через отдельно прописанные правй и левый поиск
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.left_search(nums, target)
        right = self.right_search(nums, target)
        if nums[left] != target or nums[right] != target:
            return [-1, -1]
        return [left, right]

    def left_search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def right_search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return l


# решение, написанное прямо на пробном (с использованием только прпвого поиска)
class Solution_1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.right_search(nums, target - 1)
        if nums[left] == target:
            left -= 1
        right = self.right_search(nums, target)
        if right < len(nums) and nums[right] == target:  # wtf
            return [left + 1, right] if left != right else [right, right]
        return [-1, -1]

    def right_search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] < target:
                # так как поиск правый, то можно просто l = mid,
                # и все сойдется, но не будет выходить за границы масиива
                l = mid + 1
            elif nums[mid] == target:
                l = mid
            else:
                r = mid - 1
        return l


s = Solution()

print(
    s.right_search(
        [2, 2], 3
    )
)
