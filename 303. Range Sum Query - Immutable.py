class NumArray:

    def __init__(self, nums: list[int]):
        prefs = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefs.append(cur_sum)
        self._prefs = prefs

    def sumRange(self, left: int, right: int) -> int:
        before = self._prefs[left - 1] if left > 0 else 0
        return self._prefs[right] - before


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
