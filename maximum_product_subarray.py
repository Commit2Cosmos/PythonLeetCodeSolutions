from typing import List



class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min, cur_max = 1, 1
        res = nums[0]

        for i in nums:

            tmp = cur_max * i
            cur_max = max(tmp, cur_min * i, i)
            cur_min = min(tmp, cur_min * i, i)

            res = max(res, cur_max)

        return res


nums = [2,-2,0,-2,4]


sol = Solution()
print(sol.maxProduct(nums))