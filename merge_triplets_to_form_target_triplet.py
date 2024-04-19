from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trip = [0,0,0]
        for t in triplets:
            flag = True

            for i in range(3):
                if t[i] > target[i]:
                    flag = False
                    break
                
            if flag:
                trip = [max(a, b) for a, b in zip(trip, t)]
                if trip == target:
                    return True
                
        return False
    

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]


sol = Solution()
print(sol.mergeTriplets(triplets, target))