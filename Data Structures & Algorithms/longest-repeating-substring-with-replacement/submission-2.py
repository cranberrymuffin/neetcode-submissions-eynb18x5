class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        freqs = {}
        longest = 0
        for j in range(len(s)):
            if s[j] in freqs:
                freqs[s[j]] += 1
            else:
                freqs[s[j]] = 1
            mostCommonOccurrances = 0
            mostCommon = ''

            for c, freq in freqs.items():
                if freq > mostCommonOccurrances:
                    mostCommon = c
                    mostCommonOccurrances = freq
            
            replacementsLeft = k
            for c, freq in freqs.items():
                if c != mostCommon:
                    replacementsLeft -= freq

            if replacementsLeft < 0:
                freqs[s[i]] -= 1
                if freqs[s[i]] == 0:
                    del freqs[s[i]]
                i+= 1
            longest = max(longest, j - i + 1)

        return longest

        
            
        