class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif s[0] == '0':
            return 0
        elif len(s) >= 2 and int(s[0:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        elif int(s[0:1]) > 0:
            return self.numDecodings(s[1:])
            
        