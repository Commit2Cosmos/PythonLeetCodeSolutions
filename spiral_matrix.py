from typing import List


class Solution:
    def spiralOrderDFS(self, matrix: List[List[int]]) -> List[int]:

        ROWS_NUM, COLS_NUM = len(matrix), len(matrix[0])
        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]
        
        d = 0

        curr = (0,0)
        visited = set()
        visited.add(curr)
        res = [matrix[0][0]]
 
        while True:
            flag = False
            for idx in range(4):

                dx, dy = DIRS[(d+idx)%4]
                i = curr[0] + dx
                j = curr[1] + dy

                if (i not in range(ROWS_NUM)) or (j not in range(COLS_NUM)) or (i, j) in visited:
                    continue
                
                
                d = (d+idx)%4
                visited.add((i, j))
                res.append(matrix[i][j])

                curr = (i,j)
                flag = True
                break

            if not flag:
                break
        
        return res
    

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS_NUM, COLS_NUM = len(matrix), len(matrix[0])

        res = []

        right = 0
        down = COLS_NUM-1
        left = ROWS_NUM-1
        up = 0

        while ROWS_NUM*COLS_NUM > len(res):

            for i in range(up, down+1):
                res.append(matrix[right][i])
            
            right += 1

            for i in range(right, left+1):
                res.append(matrix[i][down])
            
            down -= 1

            if left >= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[left][i])
                
                left -= 1

            if down >= up:
                for i in range(left, right-1, -1):
                    res.append(matrix[i][up])
            
                up += 1

        
        return res




matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]


sol = Solution()
print(sol.spiralOrder(matrix))