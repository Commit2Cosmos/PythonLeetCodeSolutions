class Solution:
    def getSum(self, a: int, b: int) -> int:
        sm = a^b
        rem = (a&b) << 1 

        while rem != 0:
            temp = sm
            sm = sm^rem
            rem = (temp&rem) << 1

        return sm
    

a = 7
b = 2


sol = Solution()
print(sol.getSum(a, b))