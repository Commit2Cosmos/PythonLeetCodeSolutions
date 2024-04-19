from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.nums = nums


    def add(self, val: int) -> int:

        if len(nums) < k:
            heapq.heappush(self.nums, val)
            return self.nums[0]

        heapq.heappushpop(self.nums, val)
        return self.nums[0]


k = 2
nums = [0]


obj = KthLargest(k, nums)

obj.add(-1);   # return 4
obj.add(5);   # return 5
obj.add(10);  # return 5
obj.add(9);   # return 8
obj.add(4);   # return 8