from typing import List



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps: List[set] = []

        for e in edges:
            flag = True
            for s in comps:
                if e[0] in s or e[1] in s:
                    s.add(e[0])
                    s.add(e[1])
                    flag = False
                    break
            
            if flag:
                comps.append(set(e))
        
        tot = 0
        for s in comps:
            tot += len(s)

        return len(comps) + n - tot


            


n=3
edges=[[0,1], [0,2]]


sol = Solution()
print(sol.countComponents(n, edges))
