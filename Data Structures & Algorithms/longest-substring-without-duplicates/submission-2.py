class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vals = {}
        start = 0
        length = 0
        for i, c in enumerate(s):
            if c in vals and vals[c] >= start:
                start = vals[c] + 1
            length = max(length, i - start + 1)
            vals[c] = i

        return length

        