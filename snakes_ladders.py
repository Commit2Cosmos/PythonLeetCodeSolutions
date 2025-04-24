from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = len(board)
        visited = set()
        nodes = deque([(1, 0)])
        goal = l**2

        while nodes:
            n, count = nodes.pop()

            if n == goal:
                return count


            for i in range(n+1, min(n+7, goal+1)):
                if i in visited:
                    continue

                visited.add(i)

                r, c = self.num_to_coord(l, i)
                
                if board[r][c] == -1:
                    nodes.appendleft((i, count+1))
                else:
                    nodes.appendleft((board[r][c], count+1))

        
        return -1


    def num_to_coord(self, n, c) -> tuple[int, int]:
        row = n-1 - (c-1)//n
        col = (c-1) % n

        if (n-1-row)%2 == 1:
            col = n-1 - col
        
        return (int(row), int(col))
    
sol = Solution()
print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))