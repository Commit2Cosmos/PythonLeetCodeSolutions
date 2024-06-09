class Solution:
    def longestPalindrome(self, s: str) -> str:

        def pal_count(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]


        
        res = ''

        for i in range(len(s)):
            even = pal_count(i, i+1)
            odd = pal_count(i, i)

            res = max(res, even, odd, key=len)

        return res
    



s = "babad"

sol = Solution()
print(sol.longestPalindrome(s))