class Solution:
    def freqMap(self, string):
        freqMap = [0] * 26
        for c in string:
            print(len(freqMap))
            freqMap[ord(c) - ord('a')] += 1
        return str(freqMap)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            freq = self.freqMap(string)
            if freq in groups:
                groups[freq].append(string)
            else:
                groups[freq] = [string]
        result = []
        for key, value in groups.items():
            result.append(value)
        return result


        