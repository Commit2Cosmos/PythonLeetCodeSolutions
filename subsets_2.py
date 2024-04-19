from typing import List



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()
        temp = []

        def recur(idx = 0):
            res.add(tuple(temp))
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                recur(i+1)
                temp.pop()
        recur()
        return res



nums = [1,2,2]

sol = Solution()
print(sol.subsetsWithDup(nums))
# print(sol.subsetsWithDup2(nums))