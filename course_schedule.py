from typing import List
from collections import defaultdict



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        if not prerequisites:
            return True
        
        premap = defaultdict(lambda: [])

        for c,p in prerequisites:
            premap[c].append(p)

        del c,p
        
        # print(premap.items())

        visset = set()

        def recur(i: int):
            
            if i in visset:
                return False
            
            visset.add(i)

            for c in premap[i]:
                if not recur(c, visset):
                    return False
                
            visset.remove(i)
            premap[i] = []
            
            return True
            

        for i in range(numCourses):
            if not recur(i):
                return False
            
        return True
            



numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]


sol = Solution()
print(sol.canFinish(numCourses, prerequisites))