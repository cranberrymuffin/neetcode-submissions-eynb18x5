class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        for c in s:
            if c in sChars:
                sChars[c] += 1
            else:
                sChars[c] = 1
        for c in t:
            if c in sChars:
                sChars[c] -=1
                if sChars[c] == 0:
                    del sChars[c]
            else:
                return False
        return len(sChars) == 0
        
        