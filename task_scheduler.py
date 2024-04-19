from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = list(Counter(tasks).values())

        heap = []
        queue = []
        res = 0

        for num in c:
            heapq.heappush(heap, -num)


        while heap or queue:
            if heap:
                high = heapq.heappop(heap) + 1
                if high < 0:
                    queue.append((high, res + n))

            if queue:
                if queue[0][1] == res:
                    heapq.heappush(heap, queue.pop(0)[0])

            res += 1

        return res


tasks = ["A","A","A", "B","B","B"]
n = 3

sol = Solution()
print(sol.leastInterval(tasks, n))