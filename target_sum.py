from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        l = len(nums)
        memo = {}
        
        def recur(i, tot):
            if i == l:
                if target == tot:
                    return 1
                else:
                    return 0
            

            if i in memo:
                if tot in memo[i]:
                    return memo[i][tot]
            else:
                memo[i] = {}

            memo[i][tot] = recur(i+1, tot + nums[i]) + recur(i+1, tot - nums[i])

            return memo[i][tot]


        return recur(0, 0)



nums = [1,0]
target = 1


sol = Solution()
print(sol.findTargetSumWays(nums, target))