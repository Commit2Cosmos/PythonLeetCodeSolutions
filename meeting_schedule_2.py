from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0

        start = [t[0] for t in intervals]
        end = [t[1] for t in intervals]

        start.sort()
        end.sort()

        s_point = 0
        e_point = 0

        while s_point < len(intervals):
            if start[s_point] < end[e_point]:
                count += 1
                s_point += 1
                res = max(res, count)

            else:
                count -= 1
                e_point += 1
            

        return res
    
    

intervals = [(0,40),(5,10),(15,20)]

sol = Solution()
print(sol.minMeetingRooms(intervals))