from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS_recur(self, nums: List[int]) -> int:

        def recur(i, curr):

            if len(curr) >= 2 and curr[-1] <= curr[-2]:
                return len(curr) - 1
            
            if i == len(nums):
                return len(curr)
            
            return max(recur(i+1, [*curr, nums[i]]), recur(i+1, curr))
        

        return recur(0, [])
    

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        memo = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    memo[i] = max(1+memo[j], memo[i])

        return max(memo)
    

    def lengthOfLIS_bisect(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                i = bisect_left(sub, num)
                sub[i] = num

        return len(sub)


nums = [10,9,2,5,3,7,101,18]

sol = Solution()
print(sol.lengthOfLIS(nums))