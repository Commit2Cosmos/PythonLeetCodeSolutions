from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)

        distances = [None] * n

        def calculate_distance(x, y):
            return x**2 + y**2
        

        for (i, point) in enumerate(points):
            distances[i] = (calculate_distance(point[0], point[1]), i)
        
        heapq.heapify(distances)

        return [points[idx] for (_, idx) in heapq.nsmallest(k, distances)]



    
sol = Solution()

points = [[1,3],[-2,2]]
k = 1

sol.kClosest(points, k)