from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #* sort the intervals
        intervals.sort(key = lambda i: i[1])
        
        res = 0

        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                res += 1
            
            else:
                last_end = intervals[i][1]
            
        
        return res




intervals = [[1,2],[2,3]]

sol = Solution()
print(sol.eraseOverlapIntervals(intervals))