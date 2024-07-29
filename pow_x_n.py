class Solution:
    def myPow_recur(self, x: float, n: int) -> float:

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
    

    def myPow_iter(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        result = 1

        flag = True
        if n < 0:
            flag = False
            n = -n
        
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
            
        return result if flag else 1/result



sol = Solution()
print(sol.myPow_iter(2, 4))