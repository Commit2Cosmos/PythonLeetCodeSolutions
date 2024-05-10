from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parents = [i for i in range(1, len(edges)+1)]
        rank = [1] * len(edges)


        for e in edges:
            if parents[e[1]-1] == parents[e[0]-1]:
                return e
            
            if rank[parents[e[0]-1]-1] >= rank[parents[e[1]-1]-1]:
                parents[e[1]-1] = parents[e[0]-1]
                rank[parents[e[0]-1]-1] += 1
            else:
                parents[e[0]-1] = parents[e[1]-1]
                rank[parents[e[1]-1]-1] += 1

            print(parents)


edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]

sol = Solution()
print(sol.findRedundantConnection(edges))