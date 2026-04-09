class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqMap = {}

        for c in s:
            if c in freqMap:
                freqMap[c] += 1
            else:
                freqMap[c] = 1
        
        for c in t:
            if c in freqMap:
                freqMap[c] -= 1
                if(freqMap[c] == 0):
                    del freqMap[c]
            else:
                return False
        
        return True
        