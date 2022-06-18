from typing import List


class Solution:
    # суммируем числа в массиве
    # и для каждой суммы сохраняем остаток от деления в словарь
    # если в будущем встретится сумма,
    # остаток от деления которой уже встречался,
    # значит разница между этими суммами делится на K
    def checkSubarraySum_1(self, nums: List[int], k: int) -> bool:
        rem = 0
        prefs = {0: -1}
        for i, num in enumerate(nums):
            rem += num
            rem = rem % k
            if rem in prefs:
                if i - prefs[rem] >= 2:
                    return True
            if rem not in prefs:
                prefs[rem] = i
        return False
