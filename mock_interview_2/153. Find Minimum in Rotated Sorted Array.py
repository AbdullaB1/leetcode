from typing import List


class Solution:
    # более хитрое решение из комментариев
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

    # гаписанное мной решение
    def findMin_1(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[l]
        return nums[l]
