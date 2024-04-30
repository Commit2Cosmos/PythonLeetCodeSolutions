class MinStack:

    def __init__(self):
        self.q = []
        self.min_q = []
        

    def push(self, val: int) -> None:
        self.q.append(val)

        if len(self.min_q) > 0:
            if val < self.min_q[-1]:
                self.min_q.append(val)
            else:
                self.min_q.append(self.min_q[-1])

        else:
            self.min_q.append(val)
            

    def pop(self) -> None:
        self.q.pop()
        self.min_q.pop()

        

    def top(self) -> int:
        return self.q[-1]
        

    def getMin(self) -> int:
        return self.min_q[-1]




stack = MinStack()

print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))
print(stack.getMin())
print(stack.pop())
print(stack.top())
print(stack.getMin())