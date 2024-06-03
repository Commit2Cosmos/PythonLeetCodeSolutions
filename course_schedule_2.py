from typing import List
from collections import defaultdict



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        premap = defaultdict(lambda: [])
        res = []

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
                if not recur(c):
                    return False
                
            visset.remove(i)
            premap[i] = []
            if i not in res:
                res.append(i)
            return True
            

        for i in range(numCourses):
            if not recur(i):
                return []
            
        return res
            



numCourses = 1
prerequisites = []


sol = Solution()
print(sol.findOrder(numCourses, prerequisites))