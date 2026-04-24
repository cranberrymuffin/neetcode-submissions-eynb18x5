class Solution:
    decodings = {}
    def numDecodings(self, s: str) -> int:
        if s in self.decodings:
            return self.decodings[s]
        elif len(s) > 0 and s[0] == '0':
            self.decodings[s]=0
        elif len(s) <= 1:
            self.decodings[s] = 1
        else:
            if int(s[:2]) <= 26:
                self.decodings[s] = self.numDecodings(s[2:]) + self.numDecodings(s[1:])
            else:
                self.decodings[s] = self.numDecodings(s[1:])
        return self.decodings[s]