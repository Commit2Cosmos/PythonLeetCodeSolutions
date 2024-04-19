from typing import List
from collections import Counter
import heapq 


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cards = dict(Counter(hand))

        minH = list(cards.keys())
        heapq.heapify(minH)

        while minH:
            min_key = minH[0]

            for i in range(min_key, min_key+groupSize):
                if i not in cards:
                    return False
                
                cards[i] -= 1

                if cards[i] == 0:
                    heapq.heappop(minH)

            
        return True
    

hand = [3,4,7,4,6,3,6,5,2,8]

sol = Solution()
print(sol.isNStraightHand(hand, 2))