import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        vals = []
        
        for key, value in freq.items():
            vals.append((value, key))

        heapq.heapify_max(vals)
        result = []
        for i in range(k):
            result.append(heapq.heappop_max(vals)[1])
        
        return result

        

        