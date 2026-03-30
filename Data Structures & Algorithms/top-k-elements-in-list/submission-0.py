class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        maxFreq = 0
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
            maxFreq = max(maxFreq, freqMap[num])
        buckets = []
        for i in range(maxFreq + 1):
            buckets.append(set())
        for element, freq in freqMap.items():
            buckets[freq].add(element)
        ret = []
        i = len(buckets) - 1
        while len(ret) < k:
            for item in buckets[i]:
                ret.append(item)
                if len(ret) == k:
                    break
            
            i-=1
            
        return ret