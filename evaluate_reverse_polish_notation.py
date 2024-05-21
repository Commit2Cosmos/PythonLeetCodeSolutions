from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ['+', '-', '*', '/']:
                last = stack.pop()
                tot = int(eval(f"{stack.pop()}{t}{last}"))
                stack.append(tot)
            else:
                stack.append(t)

        return stack[0]


tokens = ["2","3","11","+","5","-","*"]

sol = Solution()
print(sol.evalRPN(tokens))
        