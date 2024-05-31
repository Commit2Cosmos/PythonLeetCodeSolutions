from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [None for _ in range(len(s)+1)]
        memo[-1] = True

        def recur(start, end):

            if memo[start] is not None:
                return memo[start]

            # if start == len(s):
            #     return True

            if end > len(s):
                memo[start] = False
            
            elif s[start:end] in wordDict:
                memo[start] = recur(end, end+1) or recur(start, end+1)
            
            return recur(start, end+1)
        

        return recur(0, 1)




s = "applepenapple"
wordDict = ["appl","apple","pen"]


sol = Solution()
print(sol.wordBreak(s, wordDict))