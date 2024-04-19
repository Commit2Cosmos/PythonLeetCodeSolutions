from typing import List
import heapq

class Solution:    
    def build_mst(self, points: List[List[int]]) -> int:

        n = len(points)

        #* calculate manhattan distance between points
        def calculate_weights():

            distances = [[0]*n for _ in range(n)]

            def manh_dist(arr1, arr2):
                return abs(arr1[0]-arr2[0]) + abs(arr1[1]-arr2[1])
            
            for i in range(n):
                for j in range(i+1, n):
                    dist = manh_dist(points[i], points[j])
                    distances[i][j] = dist
                    distances[j][i] = dist
            return distances


        weights = calculate_weights()

        #* verices (i.e. tuple of edges) included in Minimum Spanning Tree
        mst = set()

        visited = [False] * n

        #* weight, node1, node2
        starting_node = 0
        edges = [(0, starting_node, starting_node)]

        while edges:
            _, node1, node2 = heapq.heappop(edges)

            if not visited[node2]:
                visited[node2] = True
                mst.add((node1, node2))

                #* add all posible edges of node2
                for i in range(n):
                    if not visited[i]:
                        heapq.heappush(edges, (weights[node2][i], node2, i))

                    
        return mst
    

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        #* calculate manhattan distance between points
        def calculate_weights():

            distances = [[0]*n for _ in range(n)]

            def manh_dist(arr1, arr2):
                return abs(arr1[0]-arr2[0]) + abs(arr1[1]-arr2[1])
            
            for i in range(n):
                for j in range(i+1, n):
                    dist = manh_dist(points[i], points[j])
                    distances[i][j] = dist
                    distances[j][i] = dist
            return distances

        weights = calculate_weights()

        res = 0
        visited = [False] * n

        #* weight, node1, node2
        starting_node = 0
        edges = [(0, starting_node)]


        while edges:
            weight, node2 = heapq.heappop(edges)

            if not visited[node2]:
                visited[node2] = True
                res += weight

                #* add all posible edges of node2
                for i in range(n):
                    if not visited[i]:
                        heapq.heappush(edges, (weights[node2][i], i))

                    
        return res
                






sol = Solution()

points = [[3,12],[-2,5],[-4,1]]

print(sol.minCostConnectPoints(points))
# print(sol.build_mst(points))