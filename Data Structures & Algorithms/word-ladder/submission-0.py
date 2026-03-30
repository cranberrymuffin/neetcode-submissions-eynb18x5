class Solution:
    def differenceOf1(self, beginWord: str, endWord: str) -> bool:
        difference = 0
        for c1, c2 in zip(beginWord, endWord):
            if c1 != c2:
                difference += 1
            if(difference > 1):
                return False
        return len(beginWord) == len(endWord)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = self.ladderLengthHelper(beginWord, endWord, wordList)
        if res == float('inf'):
            return 0
        return res

    def ladderLengthHelper(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        length = float('inf')
        for word in wordList:
            if word != beginWord and self.differenceOf1(beginWord, word):
                print(beginWord + " " + word)
                length = min(length, 1 + self.ladderLengthHelper(word, endWord, [x for x in wordList if x != word]))
        return length
        