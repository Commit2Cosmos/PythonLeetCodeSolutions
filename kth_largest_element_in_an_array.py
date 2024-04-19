from typing import List
import heapq
import random


class Solution:
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
            
        return heapq.heappop(nums)
    

    def findKthLargestQuick(self, nums: List[int], k: int) -> int:

        def recur(nums: List[int], k: int):
            # print(nums)
            pivot = random.choice(nums)
            # print(pivot)

            less, equal, greater = [], [], []

            for n in nums:
                if n == pivot:
                    equal.append(n)
                elif n > pivot:
                    greater.append(n)
                else:
                    less.append(n)

            # print(less, equal, greater)
            # print("k:", k)
            
            if k <= len(greater):
                return recur(greater, k)
            
            if k <= len(greater) + len(equal):
                return pivot
            
            return recur(less, k - len(greater) - len(equal))
        
        return recur(nums, k)




nums = [3,2,1,5,6,4]
k = 2

sol = Solution()
print(sol.findKthLargestQuick(nums, k))

nums.sort()
print(nums)