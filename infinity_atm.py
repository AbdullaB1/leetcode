from collections import defaultdict
from typing import ChainMap, List
import math


def atm_machine(target: int, bills: defaultdict) -> List[int]:
    cache = [math.inf] * (target + 1)
    cache[0] = 0
    traverse(cache, target, bills)
    if math.isinf(cache[target]):
        return None
    result = []
    while target > 0:
        for bill in bills:
            # если позади нас есть сумма, до которой мы может допрыгнуть и сумма купюр в ней на 1 меньше,
            # значит эта купюря попадает в рузльтат, а мы будем уже прыгать дальше от этой суммы
            if target - bill >= 0 and cache[target - bill] == cache[target] - 1:
                target -= bill
                result.append(bill)
                break

    print(cache)
    print(result)
    return cache[target]


def traverse(cache: List[int], target: int, bills: List[int]):
    for m in range(1, target + 1):
        for bill in bills:
            if m - bill >= 0 and cache[m] > cache[m - bill] + 1:
                cache[m] = cache[m - bill] + 1


print(
    atm_machine(130, defaultdict(int, {100: 2, 10: 10, 60: 16}))
)
