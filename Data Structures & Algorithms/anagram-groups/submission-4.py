class Solution:
    def getKey(self, string: str) -> str:
        key = [0] * 26
        for c in string:
            key[ord(c) - ord('a')] += 1
        return str(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = self.getKey(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        result = []
        for key, value in groups.items():
            result.append(value)
        
        return result
        