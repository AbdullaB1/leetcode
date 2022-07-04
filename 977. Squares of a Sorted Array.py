class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        
        left = 0
        right = len(nums) - 1
        
        result = [0] * len(nums)
        index = len(nums) - 1
        
        while left <= right:
            if nums[left] >= nums[right]:
                result[index] = nums[left]
                left += 1
            else:
                result[index] = nums[right]
                right -= 1
            index -= 1
        
        return result
    
    
class Solution:
    """если нужно сделать через yield, то это решение подойдёт лучше"""
    def sortedSquares(self, nums: list[int]) -> list[int]:
        min_idx, _ = min(enumerate(nums), key=lambda x: abs(x[1]))
        result = [nums[min_idx] ** 2]
        l = min_idx - 1
        r = min_idx + 1
        while l >= 0 and r < len(nums):
            if abs(nums[l]) < abs(nums[r]):
                result.append(nums[l] ** 2)
                l -= 1
            else:
                result.append(nums[r] ** 2)
                r += 1
        while l >= 0:
            result.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            result.append(nums[r] ** 2)
            r += 1
        return result
    