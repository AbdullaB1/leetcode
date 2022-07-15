from collections import deque


class Solution:
    """она в премиуме, но это рещение проверено на правильность"""
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i, j))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while q:
            for _ in range(len(q)):
                curr_i, curr_j = q.popleft()
                for xdel, ydel in zip(dx, dy):
                    if 0 <= curr_i + xdel < rows and 0 <= curr_j + ydel < cols and rooms[curr_i + xdel][curr_j + ydel] != -1:
                        if rooms[curr_i][curr_j] + 1 < rooms[curr_i + xdel][curr_j + ydel]:
                            rooms[curr_i + xdel][curr_j + ydel] = rooms[curr_i][curr_j] + 1
                            q.append((curr_i + xdel, curr_j + ydel))
