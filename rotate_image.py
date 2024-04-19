from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(int(N/2)):
            for j in range(i, N-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = temp




matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


Solution.rotate(Solution, matrix)

print(matrix)