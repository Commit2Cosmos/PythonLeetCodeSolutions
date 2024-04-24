class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0, 0

        for l in s:
            if l == "(":
                min_left += 1
                max_left += 1

            elif l == ")":
                min_left -= 1
                max_left -= 1
            
            else:
                min_left -= 1
                max_left += 1
            
            if max_left < 0:
                return False
            
            if min_left < 0:
                min_left = 0
        
        return True if min_left == 0 else False

                


s = "(***)"

sol = Solution()
print(sol.checkValidString(s))