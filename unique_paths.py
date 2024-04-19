class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m-1,n-1):1}

        def helper(i: int, j: int):
            
            if (i not in range(m)) or (j not in range(n)):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            counter = 0
            counter += helper(i+1, j)
            counter += helper(i, j+1)

            memo[(i,j)] = counter

            return counter
        

        return helper(0, 0)




    


sol = Solution()

print(sol.uniquePaths(3, 7))