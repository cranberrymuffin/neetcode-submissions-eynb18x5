class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = [0] * (ord('z') + 1);
        for c in s:
            charCount[ord(c)] = charCount[ord(c)] + 1
        for c in t:
            charCount[ord(c)] = charCount[ord(c)] - 1
        
        return not any(charCount)

        