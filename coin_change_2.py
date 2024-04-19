from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def recur_top_down(tot: int, n: int, memo):

            if tot == 0:
                memo[n][tot] = 1
                return 1
            
            if n == 0 or tot < 0:
                return 0
            
            if not memo[n][tot]:
                memo[n][tot] = recur_top_down(tot-coins[n-1], n, memo) + recur_top_down(tot, n-1, memo)

            return memo[n][tot]
        

        def recur_bottom_up(tot: int, n: int):

            memo = [[0]*(tot+1) for _ in range(n_coins+1)]
            memo[0][0] = 1

            for i in range(1, n+1):
                for j in range(tot+1):
                    memo[i][j] += memo[i-1][j]

                    if j - coins[i-1] >= 0:
                        memo[i][j] += memo[i][j - coins[i-1]]

            return memo[n][tot]

        n_coins = len(coins)

        # memo_top = [[None]*(amount+1) for _ in range(n_coins+1)]

        return recur_bottom_up(amount, n_coins)
    


coins = [1,2,5]
amount = 5

sol = Solution()
print(sol.change(amount, coins))