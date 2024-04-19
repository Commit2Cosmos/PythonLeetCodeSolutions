from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        adj_mat = dict()

        for (s, t, w) in times:
            s -= 1
            t -= 1
            if s not in adj_mat:
                adj_mat[s] = {}

            adj_mat[s][t] = w

        # print(adj_mat)

        #* shortest path three
        sptSet = [False] * n
        #* distance, node #
        distances = [float('inf')] * n

        distances[k] = 0

        for i in range(n):

            #! find min distance
            min_dist = float('inf')

            u = None

            for i,d in enumerate(distances):
                if min_dist > d and not sptSet[i]:
                    min_dist = d
                    u = i

            if u is None:
                return -1

            sptSet[u] = True


            if u in adj_mat:
                for (t,w) in adj_mat[u].items():
                    if distances[t] > distances[u] + w and not sptSet[t]:
                        distances[t] = distances[u] + w
                

        return max(distances) if all(sptSet) else -1



times = [[1,2,1],[2,3,2],[1,3,2]]
n = 3
k = 1
    

sol = Solution()
print(sol.networkDelayTime(times, n, k))