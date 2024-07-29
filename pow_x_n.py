import math

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recur(x, n):

            if x == 0:
                return 0
            
            if n == 0:
                return 1
            
            p = recur(x, n//2)

            if n%2==1:
                return p*p*x
            
            return p*p
        
        res = recur(x, abs(n))

        return res if n>=0 else 1/res


sol = Solution()
print(sol.myPow(2, 4))