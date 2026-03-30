class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        maxFreq = 0
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            maxFreq = max(freq[num], maxFreq)
        
        buckets = []
        for i in range(maxFreq):
            buckets.append([])

        for num, frequency in freq.items():
            buckets[frequency - 1].append(num)

        result = []
        for i in range (len(buckets) - 1, -1, -1):
            result += buckets[i]
            if len(result) == k:
                return result
        return result