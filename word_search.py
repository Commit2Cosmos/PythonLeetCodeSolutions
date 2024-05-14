from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS = len(board)
        COLS = len(board[0])

        visited=set()

        def recur(i, j, w):

            if len(visited) == len(word):
                return True

            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != word[w] or (i, j) in visited:
                return False

            is_word = False

            visited.add((i, j))
            for (di, dj) in DIRS:
                is_word = is_word or recur(i+di, j+dj, w+1)
            visited.remove((i, j))

            return is_word


        for i in range(ROWS):
            for j in range(COLS):
                if recur(i, j, 0):
                    return True
                    
        return False
    


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

sol = Solution()
print(sol.exist(board, word))