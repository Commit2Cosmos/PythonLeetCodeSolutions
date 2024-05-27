class Solution:
    def countSubstrings_bruteForce(self, s: str) -> int:

        res = 0

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1

            return True



        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    res += 1

        return res
    

    def countSubstrings(self, s: str) -> int:

        def pal_count(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                print(s[left:right])

            return count


        
        res = 0

        for i in range(len(s)):
            even = pal_count(i, i+1)
            odd = pal_count(i, i)

            res += even + odd

        return res





s = "aaa"

sol = Solution()
print(sol.countSubstrings(s))