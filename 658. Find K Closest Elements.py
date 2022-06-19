from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        idx = self.closest_left_bin_search(arr, x)
        print(idx)
        if idx + 1 < len(arr) and abs(arr[idx] - x) > abs(arr[idx + 1] - x):
            idx += 1
        print(idx)
        result = deque([arr[idx]])
        res_l, res_r = idx - 1, idx + 1
        while len(result) < k and res_l >= 0 and res_r < len(arr):
            if abs(arr[res_l] - x) <= abs(arr[res_r] - x):
                result.appendleft(arr[res_l])
                res_l -= 1
            else:
                result.append(arr[res_r])
                res_r += 1
        
        while len(result) < k and res_l >= 0:
            result.appendleft(arr[res_l])
            res_l -= 1
            
        while len(result) < k and res_r < len(arr):
            result.append(arr[res_r])
            res_r += 1
        return result
    
    # нахождение ближайшего элемента в итоге проще делать нахождением последнего меньшего числа
    def closest_left_bin_search(self, arr: list[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l
    
    # тоже работает, но например на [1, 3], 2, 1 выдает 3, а не 1,
    # что по логике правильно, но литкод просит дать в таком случа обязатлеьно 1
    def bin_search(self, arr: list[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


s = Solution()
print(
    s.bin_search(
        [1, 4], 2,
    ),
)

