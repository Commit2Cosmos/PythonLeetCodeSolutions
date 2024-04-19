from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            #* no overlap
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            #* new interval starts after current interval ends
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #* overlap 
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]


        res.append(newInterval)

        return res


intervals = [[1,5], [6,8]]
newInterval = [2,3]

sol = Solution()
print(sol.insert(intervals, newInterval))