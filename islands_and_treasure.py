from typing import List

from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #* find all 0s

        q = deque([])

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,1))
        

        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            r, c, dist = q.popleft()

            for d in DIRS:
                row = r + d[0]
                col = c + d[1]

                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] > 10000:
                    grid[row][col] = dist
                    q.append((row, col, dist+1))
        
        return grid








gas = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]


sol = Solution()
print(sol.islandsAndTreasure(gas))
