from typing import List
import math


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        if abs(target) > nums_sum:
            return 0
        results = [0] * (nums_sum * 2 + 1)
        n = len(results)
        # вдргу первое число 0, тогда на нулевой позиции должен быть 2 пути, а не 1
        results[nums_sum + nums[0]] += 1
        results[nums_sum - nums[0]] += 1
        for i in range(1, len(nums)):
            temp = [0] * len(results)
            for j in range(len(results)):
                if results[j] > 0:
                    temp[j - nums[i]] += results[j]
                    temp[j + nums[i]] += results[j]
            results = temp
        return results[nums_sum + target]


# все остальные способы не проходили по времени
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        results = [0]
        for i in range(len(nums)):
            temp = []
            for j in range(len(results)):
                val = results[j]
                results[j] += nums[i]
                results.append(val - nums[i])

        target_res_count = 0
        for res in results:
            if res == target:
                target_res_count += 1
        return target_res_count

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        results = [-sum(nums)]
        res_count = 0
        if target == results[0]:
            res_count += 1
        for i in range(1, 2**len(nums)):
            current = results[i % (1 << int(math.log(i, 2)))] + \
                2 * nums[int(math.log(i, 2))]
            results.append(current)
            if target == current:
                res_count += 1
        return res_count

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(2 ** len(nums)):
            cursum = 0
            for j in range(len(nums)):
                if i & (1 << j) == 0:
                    cursum -= nums[j]
                else:
                    cursum += nums[j]
            if cursum == target:
                result += 1
        return result

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.result = 0
        self.generateSumWays(nums, target, 0, 0)
        return self.result

    def generateSumWays(self, nums: List[int], target: int, cursum: int, index: int) -> int:
        if index == len(nums):
            if cursum == target:
                self.result += 1
            return

        self.generateSumWays(nums, target, cursum + nums[index], index + 1)
        self.generateSumWays(nums, target, cursum - nums[index], index + 1)
