class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(format(n,'b'))
        counter = 0
        while n:
            n &= (n-1)
            counter += 1

        return counter

n = 3

sol = Solution()
print(sol.hammingWeight(n))