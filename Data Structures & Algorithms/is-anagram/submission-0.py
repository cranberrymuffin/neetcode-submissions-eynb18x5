class Solution:
    def frequencyMap(self, s: str) -> dict:
        to_ret = {}
        for c in s:
            if c in to_ret:
                to_ret[c] += 1
            else:
                to_ret[c] = 1
        return to_ret

    def isAnagram(self, s: str, t: str) -> bool:
        return self.frequencyMap(s) == self.frequencyMap(t)
        