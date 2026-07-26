class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        min_val = self.stack[-1]

        while len(self.stack) != 0:
            min_val = min(min_val, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp) != 0:
            self.stack.append(tmp.pop())
        
        return min_val
