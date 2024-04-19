from typing import List


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #* 1 <= res <= max(piles)
        low = 1
        high = max(piles)

        res = high


        while low <= high:

            mid = (high + low) // 2

            tot = 0
            for p in piles:
                tot += math.ceil(p / mid)
            
            if tot <= h:
                res = min(res, mid)
                high = mid - 1

            else:
                low = mid + 1

        
        return res
        

piles = [312884470]
h = 968709470


sol = Solution()
print(sol.minEatingSpeed(piles, h))