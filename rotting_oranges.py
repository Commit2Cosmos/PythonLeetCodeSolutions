from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS_NUM, COLS_NUM = len(grid), len(grid[0])
        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]

        q = deque()
        tot_1 = 0

        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                if grid[i][j] == 2:
                    q.append((i,j,0))

                elif grid[i][j] == 1:
                    tot_1 += 1


        res = 0
        
        while q:
            i, j, iter = q.popleft()

            for (dx, dy) in DIRS:
                ii = i+dx
                jj = j+dy

                if (ii not in range(ROWS_NUM)) or (jj not in range(COLS_NUM)):
                    continue
                
                if grid[ii][jj] == 1:
                    tot_1 -= 1

                    res = max(res, iter+1)

                    grid[ii][jj] = 2
                    q.append((ii,jj, iter+1))
            

        if tot_1 == 0:
            return res
        
        return -1



grid = [[2,1,1],[1,1,1],[0,1,2]]


sol = Solution()
print(sol.orangesRotting(grid))