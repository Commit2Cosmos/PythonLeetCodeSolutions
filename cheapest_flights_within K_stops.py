from typing import List



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {}

        for (s, d, cost) in flights:
            if s not in adj_list:
                adj_list[s] = {}
            
            adj_list[s][d] = cost

        
        min_cost = [float('inf')] * n
        temp = min_cost.copy()
        min_cost[src] = 0

        
        for _ in range(k+1):
            for (s, d) in adj_list.items():
                for (d, cost) in d.items():
                    if temp[d] > min_cost[s] + cost:
                        temp[d] = cost + min_cost[s]

            min_cost = temp.copy()

        return min_cost[dst] if min_cost[dst] < float('inf') else -1


        


n = 7
flights = [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]]
src = 2
dst = 4
k = 1


sol = Solution()
print(sol.findCheapestPrice(n, flights, src, dst, k))