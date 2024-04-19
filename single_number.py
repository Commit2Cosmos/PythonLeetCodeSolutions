from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans


nums = [4,1,2,1,2]


sol = Solution()
print(sol.singleNumber(nums))