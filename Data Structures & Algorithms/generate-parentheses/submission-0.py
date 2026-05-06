class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def helper(openParen, closeParen):
            if openParen == closeParen == n:
                result.append("".join(stack))
            
            if openParen < n:
                stack.append("(")
                helper(openParen + 1, closeParen)
                stack.pop()
            
            if closeParen < openParen:
                stack.append(")")
                helper(openParen, closeParen + 1)
                stack.pop()
        
        helper(0,0)
        return result

        