class Solution:
    def freqMap(self, s) -> dict:
        f = {}
        for c in s:
            if c in f:
                f[c] += 1
            else:
                f[c] = 1

        return f
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            f = frozenset(self.freqMap(s).items())
            if(f not in anagrams):
                anagrams[f] = [s]
            else:
                anagrams[f].append(s)
        return anagrams.values()