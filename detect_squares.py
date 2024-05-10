from typing import List
from collections import defaultdict



class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)


    def add(self, point: List[int]) -> None:

        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point

        count = 0

        for (p0, p1), c in list(self.points.items()):
            if (abs(x - p0) != abs(y - p1)) or x==p0 or y==p1:
                continue
            
            count += c * self.points[(p0, y)] * self.points[(x, p1)]

        return count



obj = DetectSquares()
obj.add([419,351])
obj.add([798,351])
obj.add([798,730])
print(obj.count([419,730]))
# obj.add([11, 2])
# print(obj.count([11, 10]))