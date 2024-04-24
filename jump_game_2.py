from typing import List



class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        left = right = 0

        while right < len(nums)-1:
            temp = right + 1

            for i in range(left, right+1):
                right = max(right, nums[i]+i)
            
            left = temp
            res += 1

        return res

       


nums = [2,3,0,1,4]

sol = Solution()
print(sol.jump(nums))