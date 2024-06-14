from typing import List
import heapq 



class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]

        DIRS = ((1,0), (0,1), (-1,0), (0,-1))


        while min_heap:

            curr_lvl, i, j = heapq.heappop(min_heap)

            if (i,j) in visited:
                continue

            visited.add((i,j))

            if (i,j) == (ROWS-1, COLS-1):
                return curr_lvl


            for d in DIRS:
                new_i, new_j = i+d[0], j+d[1]

                if (0 <= new_i < ROWS) and (0 <= new_j < COLS):
                    heapq.heappush(min_heap, (max(grid[new_i][new_j], curr_lvl), new_i, new_j))





grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

sol = Solution()
print(sol.swimInWater(grid))