class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0
        start = 0
        end = 0
        i = 0
        for i, c in enumerate(s):
            if c in seen:
                idx = seen[c]
                if idx >= start:
                    start = idx + 1
            length = i - start + 1
            maxLength = max(maxLength, length)
            seen[c] = i
            end = i
        return  maxLength