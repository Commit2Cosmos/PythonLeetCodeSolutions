from typing import List



class Solution:
    def canPartitionDFS(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        s = s//2

        memo = {}

        def dfs(i, tot, memo):

            if i >= len(nums):
                return False
            
            if tot == s:
                return True
            
            if (i, tot) in memo:
                return memo[(i, tot)]
            
            memo[(i, tot)] = dfs(i + 1, tot + nums[i], memo) or dfs(i + 1, tot, memo)
            return memo[(i, tot)]
            
        
        return dfs(0, 0, {})
    

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        s = s//2

        memo = set()
        memo.add(0)

        for i in reversed(range(0, len(nums))):

            for existing in memo.copy():
                memo.add(existing + nums[i])
            
            if s in memo:
                return True

        return False


nums = [1,5,11,5]

sol = Solution()
print(sol.canPartition(nums))