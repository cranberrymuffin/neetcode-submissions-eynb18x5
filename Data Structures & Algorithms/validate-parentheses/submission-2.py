class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='[' or c == '{' or c == '(':
                stack.append(c)
            elif len(stack) > 0:
                pop = stack.pop()
                if c==']' and pop != '[':
                    return False
                if c=='}' and pop != '{':
                    return False
                if c==')' and pop != '(':
                    return False
            else:
                return False
        
        return len(stack) == 0
        