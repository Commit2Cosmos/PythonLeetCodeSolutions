from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS_NUM, COLS_NUM = len(grid), len(grid[0])

        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]


        def dfs_helper(i: int, j: int):

            if (i not in range(ROWS_NUM)) or (j not in range(COLS_NUM)) or (grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0
            counter = 0

            for d in DIRS:
                counter += dfs_helper(i+d[0], j+d[1])


            return counter + 1




        max_size = 0
        for i in range(ROWS_NUM):
            for j in range(COLS_NUM):
                s = dfs_helper(i, j)
                if s != 0:
                    max_size = max(max_size, s)

        return max_size

                    

sol = Solution()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))