class Solution:
    def isAlphaNumeric(self, s: str) -> bool:
        return (ord(s) >= ord('a') and ord(s) <= ord('z')) or (ord(s) >= ord('A') and ord(s) <= ord('Z')) or (ord(s) >= ord('0') and ord(s) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()

        while i < j:
            while i < len(s) and not self.isAlphaNumeric(s[i]):
                i += 1
            while j >= 0 and not self.isAlphaNumeric(s[j]):
                j -= 1   
            
            if i >= len(s) and j < 0:
                break

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        
        return True