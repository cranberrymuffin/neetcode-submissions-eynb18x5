class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canSegment = {}
        def canBreak(i, words):
            if i == len(s):
                return True
            if i in canSegment:
                return canSegment[i]
            longest_word = max(words, key=len)
            for idx in range(i, i + len(longest_word)):
                if s[i:idx + 1] in words:
                    if canBreak(idx + 1, words):
                        return True
                    else:
                        canSegment[i] = False

            return False
        return canBreak(0, set(wordDict))


        