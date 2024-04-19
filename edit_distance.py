class Solution:
    def minDistance_2(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        memo = [[0]*(len2+1) for _ in range((len1+1))]

        for idx1 in range(len1+1):
            for idx2 in range(len2+1):

                if idx1 == 0:
                    memo[idx1][idx2] = idx2

                elif idx2 == 0:
                    memo[idx1][idx2] = idx1
                
                elif word1[idx1-1] == word2[idx2-1]:
                    memo[idx1][idx2] = memo[idx1-1][idx2-1]

                else:
                    memo[idx1][idx2] = 1 + min(
                            memo[idx1][idx2-1], #* insert -> +1 len1
                            memo[idx1-1][idx2], #* remove -> +1 len2
                            memo[idx1-1][idx2-1], #* replace -> letters equal
                            )
    
        return memo[len1][len2]
    


    def minDistance(self, word1: str, word2: str) -> int:

        def minDistanceRecur(len1: int, len2: int):
            if len1 == 0:
                return len2
            
            if len2 == 0:
                return len1
            
            if word1[len1-1] == word2[len2-1]:
                return minDistanceRecur(len1-1, len2-1)
            
            #* move 1 back by default with a "cost of action" of 1
            return 1 + min(minDistanceRecur(len1, len2-1), #* insert -> +1 len1
                           minDistanceRecur(len1-1, len2), #* remove -> +1 len2
                           minDistanceRecur(len1-1, len2-1), #* replace -> letters equal
                           )


        return minDistanceRecur(len(word1), len(word2))


word1 = "a"
word2 = "b"

sol = Solution()
print(sol.minDistance_2(word1, word2))