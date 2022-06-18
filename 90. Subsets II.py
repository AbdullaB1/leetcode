from typing import List


class Solution:
    # https://leetcode.com/problems/subsets-ii/discuss/750386/Python3-DFS-solutions-to-6-different-classic-backtracking-problems-and-more
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res


class Solution_1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(2 ** len(nums)):
            cur = []
            for j in range(len(nums)):
                if i & 2 ** j != 0:
                    cur.append(nums[j])
            # print(cur)
            result.add(tuple(cur))
        return [list(res) for res in result]


s = Solution()
print(
    s.subsetsWithDup(
        [1, 2, 2]
    )
)
