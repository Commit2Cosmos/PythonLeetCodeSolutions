

class Solution:
    def numDecodings_recur(self, s: str) -> int:
        #* 1 -> 26 ; 65 -> 91

        memo = [None for _ in range(len(s)+1)]
        memo[-1] = 1

        def recur(start: int):

            if memo[start]:
                return memo[start]

            if s[start] == '0':
                return 0
            
            res = recur(start+1)

            if start+1 < len(s) and (s[start] == '1' or (s[start] == '2' and s[start+1] in '0123456')):
                res += recur(start+2)
            
            memo[start] = res
            return res
        
        return recur(0)
    

    def numDecodings(self, s: str) -> int:
        memo = [None for _ in range(len(s)+1)]
        memo[-1] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                memo[i] = 0
            
            else:
                memo[i] = memo[i+1]

            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                memo[i] += memo[i+2]

        return memo
    
            




s = "226"

sol = Solution()
print(sol.numDecodings_recur(s))