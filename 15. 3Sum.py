class Solution:    
    # без сортировки c доп памятью, более котороткое решение
    def threeSum(self, nums: list[int]) -> list[list[int]]:
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
    
    
class Solution:
    # используем идею задачи 2 sum для отсортированного массива
    # для избежания повторов не берем подряд идущие одинаковые значения для указателей i и l
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        prev_one = None
        for i in range(len(nums) - 2):
            # нет смысла идти в отсортированном массиве дальше, 
            # если первый указатель уже больше 0, так как сумма должна равняться 0
            if nums[i] > 0:
                break
            # для избежания дубликатов в ответе
            if nums[i] == prev_one:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            prev_two = None
            while l < r:
                # для избежания дубликатов в ответе
                if nums[l] == prev_two:
                    l += 1
                    continue
                curr = nums[l] + nums[r]
                if curr == target:
                    result.append([nums[i], nums[l], nums[r]])
                    # нужно обновлять prev_two именно здесь, до того как мы успели сделать l += 1
                    prev_two = nums[l]
                    l += 1
                    # r -= 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
                # prev_two = nums[l]
            prev_one = nums[i]
        return result
    