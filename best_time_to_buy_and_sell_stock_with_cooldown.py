from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def recur(i: int, can_buy: bool):

            if i >= len(prices):
                return 0
            
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            
            cooldown = recur(i+1, can_buy)

            if can_buy:
                memo[(i, True)] = max(recur(i+1, False) - prices[i], cooldown)
                
            else:
                memo[(i, False)] = max(recur(i+2, True) + prices[i], cooldown)
                
            return memo[(i, can_buy)]
            

        memo = {}
        return recur(0, True)





    
prices = [1,2,4]

sol = Solution()
print(sol.maxProfit(prices))