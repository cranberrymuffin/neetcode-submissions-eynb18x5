class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxs = {}
        longest = 0
        start = 0
        for i, c in enumerate(s):
            if c in idxs and idxs[c] >= start:
                start = idxs[c] + 1
            idxs[c] = i
            longest = max(longest, i - start + 1)

        return max(longest, start - len(s))
        
        