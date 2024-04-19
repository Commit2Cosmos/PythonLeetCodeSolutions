from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        difference_list = [a - b for a, b in zip(gas, cost)]

        if sum(difference_list) < 0:
            return -1
        
        tot = 0
        idx = 0

        for i in range(len(difference_list)):
            tot += difference_list[i]
            if tot < 0:
                tot = 0
                idx = i+1
        
        return idx


            



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

sol = Solution()
print(sol.canCompleteCircuit(gas, cost))
