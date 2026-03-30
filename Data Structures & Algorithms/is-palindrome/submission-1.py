class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i<j:
            start = s[i].lower()
            end = s[j].lower()
            if not(start >= 'a' and start <= 'z') and not(start >= '0' and start <='9'):
                i+=1
                continue
            if not(end >= 'a' and end <= 'z') and not(end >= '0' and end <='9'):
                j-=1
                continue
            if start != end:
                return False
            i+=1
            j-=1
        
        return True
        