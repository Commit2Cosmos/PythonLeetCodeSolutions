from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def recur(braces: str = '', left: int = 0, right: int = 0):
            if left > n or right > n or right > left:
                return
            
            if left == n and right == n:
                res.append(braces)
                return
            
            recur(braces + ')', left, right+1)
            recur(braces + '(', left+1, right)

        recur()

        return res


n = 3

sol = Solution()
print(sol.generateParenthesis(n))