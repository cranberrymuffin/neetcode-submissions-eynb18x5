class Solution:
    def isOpen(self, c: str) -> bool:
        return c == '{' or c == '(' or c == '['
    def isMatching(self, o:str, c:str) -> bool:
        return o == '{' and c == '}' or o == '(' and c == ')' or o == '[' and c == ']'

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if self.isOpen(c):
                stack.append(c)
            elif len(stack) == 0 or not self.isMatching(stack[len(stack) -1], c):
                return False
            else:
                stack = stack[0:len(stack) - 1]
        return len(stack) == 0

        