from typing import List
import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i

            res[i] = 1 + res[i-offset]


        return res
    

n = 8

sol = Solution()
print(sol.countBits(n))