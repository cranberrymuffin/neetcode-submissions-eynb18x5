class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [0] * (max(nums) - min(nums) + 1)

        for num in nums:
            freqs[num - min(nums)] += 1

        buckets = []
        for i in range(max(freqs)):
            buckets.append([])

        for num, freq in enumerate(freqs):
            if(freq > 0):
                buckets[freq - 1].append(num + min(nums))

        result = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        

        