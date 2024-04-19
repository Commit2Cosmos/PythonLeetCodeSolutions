from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        tot = 0
        ans = 0
        max_num = float('-inf')

        for i in nums:
            max_num = max(max_num, i)

            if tot + i < 0:
                tot = 0
            else:
                tot = tot + i
                ans = max(ans, tot)

        return ans if ans != 0 else max_num



        


nums = [-2,1,-3,4,-1,2,1,-5,4]
    
sol = Solution()
print(sol.maxSubArray(nums))