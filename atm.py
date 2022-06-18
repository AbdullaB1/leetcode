from collections import defaultdict
import math


# Time O(target * len(bills)^2)
# Space O(target * len(bills))
def atm_machine(target: int, bills: defaultdict) -> list[int]:
    memo = [math.inf] * (target + 1)
    memo_bills = [defaultdict(int)] * (target + 1)
    memo[0] = 0
    traverse(memo, target, bills, memo_bills)
    if math.isinf(memo[target]):
        return None
    # print(memo)
    # print(
    #     *zip(
    #         enumerate(memo),
    #         map(lambda x: x.items(), memo_bills)
    #     ),
    #     sep="\n"
    # )
    res = []
    for key in memo_bills[target]:
        res.extend([key] * memo_bills[target][key])
    return sorted(res)


def traverse(cache: list[int], target: int, bills: list[int], cache_bills: list[defaultdict]):
    for m in range(1, target + 1):
        for bill in bills:
            if m - bill >= 0 and cache[m] > cache[m - bill] + 1 and cache_bills[m - bill][bill] < bills[bill]:
                cache[m] = cache[m - bill] + 1
                cache_bills[m] = defaultdict(int, {**cache_bills[m - bill]})
                cache_bills[m][bill] += 1


assert atm_machine(
    1120, defaultdict(int, {1000: 2, 100: 100, 10: 100})) == [10, 10, 100, 1000]
assert atm_machine(
    130, defaultdict(int, {100: 2, 10: 10, 60: 16})) == [10, 60, 60]
assert atm_machine(
    120, defaultdict(int, {100: 1, 10: 10, 60: 2})) == [60, 60]
assert atm_machine(
    90, defaultdict(int, {15: 10, 45: 1})) == [15, 15, 15, 45]
assert atm_machine(
    120, defaultdict(int, {100: 1, 10: 10, 60: 2})) == [60, 60]
assert atm_machine(75, defaultdict(
    int, {5: 10, 15: 1, 45: 2, 30: 2})) == [30, 45]

print(
    atm_machine(7, defaultdict(int, {5: 10, 3: 2, 1: 1, 30: 2}))
)
