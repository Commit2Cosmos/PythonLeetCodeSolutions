from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def recur(arr: List = [], j = 0, summ = 0):

            if summ > target:
                return
            
            if summ == target:
                res.append(arr)
                return
            
            prev = -1
            for i in range(j, len(candidates)):
                if i != 0 and (prev == candidates[i]):
                    continue
                recur([*arr, candidates[i]], i+1, summ + candidates[i])
                prev = candidates[i]

        recur()
        return res



    
candidates = [10,1,2,7,6,1,5]
target = 8


sol = Solution()
print(sol.combinationSum2(candidates, target))