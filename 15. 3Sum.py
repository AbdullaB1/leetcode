from typing import List


class Solution:
    # используем идею задачи 2 sum
    # для избежания повторов не берем подряд идущие одинаковые значения для указателей i и l
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        prev_i = None
        for i in range(len(nums) - 2):
            # нет смысла идти в отсортированном массиве дальше,
            # если первый указатель уже больше 0, так как сумма должна равняться 0
            if nums[i] == prev_i or nums[i] > 0:
                continue
            l = i + 1
            r = len(nums) - 1
            prev_l = None
            target = - nums[i]
            while l < r:
                if nums[l] == prev_l:
                    l += 1
                    continue
                if nums[l] + nums[r] == target:
                    results.append([nums[i], nums[l], nums[r]])
                    prev_l = nums[l]
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            prev_i = nums[i]

        return results

    # без сортировки
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                seen = set()
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2]
        return res


s = Solution()
print(
    s.threeSum([-1, 0, 1, 2, -1, -4])
)
