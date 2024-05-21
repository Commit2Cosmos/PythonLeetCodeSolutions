from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        num_to_digit = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        res = []
        
        def recur(i, temp = ""):
            if i == len(digits):
                res.append(temp)
                return
            
            for l in num_to_digit[int(digits[i])]:
                for char in l:
                    temp += char
                    recur(i+1, temp)
                    temp = temp[:-1]

        recur(0)
        return res
        


digits = "23"

sol = Solution()
print(sol.letterCombinations(digits))