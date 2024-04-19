from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()

        prev = intervals[0]
        
        for i in range(1, len(intervals)):

            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
                continue


            prev = [prev[0], max(prev[1], intervals[i][1])]
        
        res.append(prev)

        return res

        




intervals = [[1,3],[2,6],[8,10],[15,18]]

sol = Solution()
print(sol.merge(intervals))