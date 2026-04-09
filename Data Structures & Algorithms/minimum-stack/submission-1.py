class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack

        if len(self.minStack) == 0:
            self.minStack = [val] + self.minStack
        else:
            self.minStack = [min(self.minStack[0], val)] + self.minStack
        

    def pop(self) -> None:
        self.stack = self.stack[1:]
        self.minStack = self.minStack[1:]

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.minStack[0]
        
