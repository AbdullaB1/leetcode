from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        result = 0
        remainders = defaultdict(int, {0: 1})
        curr_rem = 0
        for num in nums:
            curr_rem += num
            curr_rem %= k
            result += remainders[curr_rem]
            remainders[curr_rem] += 1
        return result
