class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Anagram = list(s1)
        s1Anagram.sort()
        for start in range(0, len(s2)):
            substring = list(s2[start:start+len(s1)])
            substring.sort()
            print(substring)
            print(s1Anagram)
            if substring == s1Anagram:
                return True
        return False

        