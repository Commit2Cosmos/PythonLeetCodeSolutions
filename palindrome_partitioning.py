from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []


        def is_palindrome(s):
            return s == s[::-1]


        def dfs(start: int, curr: List):

            if start == len(s):
                res.append(curr.copy())
                return


            for end in range(start+1, len(s)+1):
                if is_palindrome(s[start:end]):
                    
                    curr.append(s[start:end])
                    dfs(end, curr)
                    curr.pop()

        
        dfs(0, [])


        return res





s = "aab"

sol = Solution()
print(sol.partition(s))