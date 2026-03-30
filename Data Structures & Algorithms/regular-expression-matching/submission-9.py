class Solution:
    def isFirstCharMatch(self, s: str, p: str) -> bool:
        return len(s)>0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.')

    def isMatch(self, s: str, p: str) -> bool:
        print(s)
        print(p)
        if len(p) == 0 and len(s) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (self.isFirstCharMatch(s, p) and self.isMatch(s[1:], p))
        else:
            return self.isFirstCharMatch(s, p) and self.isMatch(s[1:], p[1:])

# s="nnn"
# p="n*"
