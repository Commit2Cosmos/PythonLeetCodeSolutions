from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):

            if i >= len(nums):
                res.append(subset.copy())
                return
            

            #* include nums[i]
            dfs(i+1, [*subset, nums[i]])

            #* not include nums[i]
            dfs(i+1, subset)
        
        dfs(0, [])

        print(res)

        return res
    

sol = Solution()

nums = [1,2,3]
sol.subsets(nums)