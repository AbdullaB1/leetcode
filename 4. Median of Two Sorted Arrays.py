import math
from typing import List


class Solution:
    # https://www.youtube.com/watch?v=q6IEA26hvXc&t=1s&ab_channel=NeetCode
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        median = (n + m) // 2

        left = 0
        right = n - 1
        while True:
            i = (left + right) // 2
            j = median - i - 2

            left_i = nums1[i] if i >= 0 else -math.inf
            right_i = nums1[i + 1] if i + 1 < n else math.inf
            left_j = nums2[j] if j >= 0 else -math.inf
            right_j = nums2[j + 1] if j + 1 < m else math.inf

            if left_i <= right_j and left_j <= right_i:
                if (n + m) % 2:
                    return min(right_i, right_j)
                return (max(left_i, left_j) + min(right_i, right_j)) / 2

            if left_i > right_j:
                right = i - 1
            else:
                left = i + 1
