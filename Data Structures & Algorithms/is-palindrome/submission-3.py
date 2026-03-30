class Solution:
    def isAlphaNumeric(self, c: str) -> bool:
        isCaps = ord(c) >= ord('A') and ord(c) <= ord('Z')
        isLowercase = ord(c) >= ord('a') and ord(c) <= ord('z')
        isNumber = ord(c) >= ord('0') and ord(c) <= ord('9')

        return isCaps or isLowercase or isNumber

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            while start < len(s) and not self.isAlphaNumeric(s[start]):
                start += 1
            while end >= 0 and not self.isAlphaNumeric(s[end]):
                end -= 1
            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            
