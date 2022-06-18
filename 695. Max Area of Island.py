from typing import List
from collections import deque


class Solution:
    # через обход в ширину
    # нужно отображать 1 в 0 перед тем, как поместить элемент в стек / очередь,
    # так как один и тот же элемент может быть вызван 2 с разных клеток,
    # что приведет к неправильному, а если заранее обнулить элемент,
    # то другая соседняя клетка уже не вызовет её
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.getAreaSize(grid, i, j))
        return max_area

    def getAreaSize(self, grid: List[List[int]], row: int, col: int) -> int:
        m = len(grid)
        n = len(grid[0])
        drow = [1, -1, 0, 0]
        dcol = [0, 0, 1, -1]
        area_size = 1
        grid[row][col] = 0
        q = deque([(row, col)])
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for i, j in zip(drow, dcol):
                    currow = row + i
                    curcol = col + j
                    if 0 <= currow < m and 0 <= curcol < n and grid[currow][curcol] == 1:
                        area_size += 1
                        grid[currow][curcol] = 0
                        q.append((currow, curcol))
        return area_size


class Solution_1:
    # через обход в ширину
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.getAreaSize(grid, i, j))
        return max_area

    def getAreaSize(self, grid: List[List[int]], row: int, col: int) -> int:
        m = len(grid)
        n = len(grid[0])
        drow = [1, -1, 0, 0]
        dcol = [0, 0, 1, -1]
        area_size = 0
        q = deque([(row, col)])
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    area_size += 1
                else:
                    continue
                for i, j in zip(drow, dcol):
                    currow = row + i
                    curcol = col + j
                    if 0 <= currow < m and 0 <= curcol < n and grid[currow][curcol] == 1:
                        q.append((currow, curcol))
        return area_size


class Solution_2:
    # через обход в глубину
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.getAreaSize(grid, i, j))
        return max_area

    def getAreaSize(self, grid: List[List[int]], row: int, col: int) -> int:
        m = len(grid)
        n = len(grid[0])
        drow = [1, 0, -1, 0]
        dcol = [0, 1, 0, -1]
        area_size = 1
        grid[row][col] = 0
        stack = [(row, col)]
        while stack:
            row, col = stack.pop()
            for i, j in zip(drow, dcol):
                currow = row + i
                curcol = col + j
                if 0 <= currow < m and 0 <= curcol < n and grid[currow][curcol] == 1:
                    area_size += 1
                    grid[currow][curcol] = 0
                    stack.append((currow, curcol))
        return area_size
