from typing import List



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        temp = []
        
        def recur(i):
            
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            
            for n in nums:
                if n in temp:
                    continue
                
                temp.append(n)
                recur(i+1)
                temp.pop()

        recur(0)

        return res
    


nums = [1,2,3]

sol = Solution()
print(sol.permute(nums))