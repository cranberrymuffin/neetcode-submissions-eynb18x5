class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceHelper(text1, text2, {})


    def longestCommonSubsequenceHelper(self, text1: str, text2: str, seen = {}) -> int:
        if((text1, text2) in seen):
            return seen[(text1, text2)]
        result = 0
        if(len(text1) == 0 or len(text2) == 0):
            result = 0
        elif(text1[0] == text2[0]):
            result = 1 + self.longestCommonSubsequenceHelper(text1[1:], text2[1:], seen)
        else:
            result = max(self.longestCommonSubsequenceHelper(text1, text2[1:], seen), 
                        self.longestCommonSubsequenceHelper(text1[1:], text2, seen),
                        self.longestCommonSubsequenceHelper(text1[1:], text2[1:], seen))
        seen[(text1, text2)] = result
        return result
         