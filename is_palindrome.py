import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        
        s= re.sub(r'[^a-zA-Z0-9]', '', s)

        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
            
        return True

        # rev_s=s[::-1]

        # if s==rev_s:
        #     return True
        # else:
        #     return False



s = "issi"

sol = Solution()
print(sol.isPalindrome(s))