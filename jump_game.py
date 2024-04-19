from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        to_reach = len(nums)-1

        dist = 1

        for i in reversed(range(len(nums)-1)):
            if nums[i] >= dist:
                to_reach = i
                dist = 1
            else:
                dist += 1

        return True if to_reach == 0 else False


nums = [1,2,0,1]


sol = Solution()
print(sol.canJump(nums))