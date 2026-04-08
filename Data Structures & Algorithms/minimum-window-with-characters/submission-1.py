class Solution:
    def containsAll(self, s: str, t: str) -> bool:
        includes = 0
        for c in t:
            if c in s:
                includes += 1
                s = s[0:s.index(c)] + s[s.index(c)+1:] 
        return includes == len(t)
            
    def minWindow(self, s: str, t: str) -> str:
        locations = {}
        start = 0
        end = 0

        result = None

        while start < len(s) and end < len(s):
            if s[start] not in t:
                start += 1
            if not self.containsAll(s[start:end + 1], t):
                end += 1
            else:
                if result == None or len(s[start:end+1]) < len(result):
                    result = s[start:end + 1]
                start += 1
        
        if result == None:
            return ""

        return result
                
        