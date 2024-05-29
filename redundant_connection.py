from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)


        def find(n):
            p = parents[n]

            while p != parents[p]:
                p = parents[p]

            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        
        for (e1, e2) in edges:
            if not union(e1, e2):
                return [e1, e2]



edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]

sol = Solution()
print(sol.findRedundantConnection(edges))