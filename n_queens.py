from typing import List



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        res = []


        def is_safe(row: int, col: int):
            #* check column
            for r in range(row):
                if board[r][col] == "Q":
                    return False
                

            rr = row
            cc = col


            #* check upper left diagonal
            while 0 <= rr and 0 <= cc:
                if board[rr][cc] == "Q":
                    return False
                rr -= 1
                cc -= 1

            rr = row
            cc = col

            #* check upper right diagonal
            while 0 <= rr and cc < n:
                if board[rr][cc] == "Q":
                    return False
                rr -= 1
                cc += 1
            
            return True



        def recur(row):
            if row == n:
                res.append([''.join(sublist) for sublist in board])
                return
            
            for c in range(n):
                if is_safe(row, c):
                    board[row][c] = "Q"
                    recur(row+1)
                    board[row][c] = "."


        recur(0)
        return res


n = 4


sol = Solution()
print(sol.solveNQueens(n))