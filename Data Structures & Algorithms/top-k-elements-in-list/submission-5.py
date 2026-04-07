class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        maxFreq = 0
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            maxFreq = max(maxFreq, freq[num])
        buckets = []
        for i in range(maxFreq):
            buckets.append([])
        for num, freq in freq.items():
            buckets[freq - 1].append(num)

        result = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if(len(result) == k):
                    return result

