class Solution:
    def isAlphaNumeric(self, c: str) -> bool:
        return (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))
    def lowercase(self, c: str)-> bool:
        if(ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return chr(ord(c) - ord('A') + ord('a'))
        return c
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while True:
            print(self.isAlphaNumeric(s[i]))
            while i < len(s) and not self.isAlphaNumeric(s[i]):
                i += 1
            while j >= 0 and not self.isAlphaNumeric(s[j]):
                j -= 1
            if i >= j or i >= len(s) or j < 0:
                return True

            if self.lowercase(s[i]) != self.lowercase(s[j]):
                return False
            i += 1
            j -= 1
