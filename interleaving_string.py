class Solution:
    # def isInterleave_recur(self, s1: str, s2: str, s3: str) -> bool:

    #     if len(s1) + len(s2) != len(s3):
    #         return False
        
    #     dp = {}

    #     def recur(p1, p2):

    #         if (p1,p2) in dp:
    #             return False

    #         if p1 == len(s1) and p2 == len(s2):
    #             return True

    #         if p1 < len(s1) and s1[p1] == s3[p1+p2] and recur(p1+1, p2):
    #             return True
            
    #         if p2 < len(s2) and s2[p2] == s3[p1+p2] and recur(p1, p2+1):
    #             return True
            
    #         dp[(p1,p2)] = False
    #         return False


    #     return recur(0,0)
    

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for p1 in range(len(s1), -1, -1):
            for p2 in range(len(s2), -1, -1):
                if p1 < len(s1) and s1[p1] == s3[p1+p2] and dp[p1+1][p2]:
                    dp[p1][p2] = True
            
                if p2 < len(s2) and s2[p2] == s3[p1+p2] and dp[p1][p2+1]:
                    dp[p1][p2] = True
        
        print(dp)
        return dp[0][0]
    

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False

    #     dp = [ [False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    #     dp[len(s1)][len(s2)] = True

    #     for i in range(len(s1), -1, -1):
    #         for j in range(len(s2), -1, -1):
    #             if i < len(s1) and s1[i] == s3[i +j] and dp[i + 1][j]:
    #                 dp[i][j] = True
    #             if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
    #                 dp[i][j] = True
    #     return dp[0][0]
                


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"


sol = Solution()
print(sol.isInterleave(s1,s2,s3))