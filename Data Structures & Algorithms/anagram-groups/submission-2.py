class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        groupedAnagrams = []
        for string in strs:
            foundGroup = False
            for group in groupedAnagrams:
                group1 = list(string)
                group1.sort()
                group2 = list(group[0])
                group2.sort()
                if group1 == group2:
                    group.append(string)
                    foundGroup = True
            if not foundGroup:
                groupedAnagrams.append([string])

        return groupedAnagrams

        