class Solution:
    def isOperand(self, string: str) -> bool:
        return string == '+' or string == '-' or string == '*' or string == '/'

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.isOperand(token):
                if token == '+':
                    a = int(stack.pop(0))
                    b = int(stack.pop(0))
                    stack = [a + b] + stack
                if token == '-':
                    a = int(stack.pop(0))
                    b = int(stack.pop(0))
                    stack = [b - a] + stack
                if token == '*':
                    a = int(stack.pop(0))
                    b = int(stack.pop(0))
                    stack = [a * b] + stack
                if token == '/':
                    a = int(stack.pop(0))
                    b = int(stack.pop(0))
                    print(b)
                    print(a)
                    stack = [b / a] + stack
            else:
                stack = [token] + stack
        
        return int(stack.pop(0))
        