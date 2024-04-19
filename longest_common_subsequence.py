class Solution:
    def longestCommonSubsequenceRecur(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        memo = [[None]*len2 for _ in range(len1)]

        def recur(idx1: int, idx2: int):
            if idx1 >= len1 or idx2 >= len2:
                return 0
            if not memo[idx1][idx2]:
                if text1[idx1] == text2[idx2]:
                    memo[idx1][idx2] = 1 + recur(idx1+1, idx2+1)
                else:
                    memo[idx1][idx2] = max(recur(idx1+1, idx2), recur(idx1, idx2+1))
                
            return memo[idx1][idx2]
            
            
        return recur(0, 0)



    def longestCommonSubsequenceIter(self, text1: str, text2: str) -> int:

        len1 = len(text1)
        len2 = len(text2)

        memo = [[0]*(len2+1) for _ in range((len1+1))]

        for idx1 in reversed(range(len1)):
            for idx2 in reversed(range(len2)):
                if text1[idx1] == text2[idx2]:
                    memo[idx1][idx2] = 1 + memo[idx1+1][idx2+1]
                else:
                    memo[idx1][idx2] = max(memo[idx1][idx2+1], memo[idx1+1][idx2])
    
        return memo[0][0]

sol = Solution()

text1 = "abc"
text2 = "abc"

print(sol.longestCommonSubsequenceIter(text1, text2))