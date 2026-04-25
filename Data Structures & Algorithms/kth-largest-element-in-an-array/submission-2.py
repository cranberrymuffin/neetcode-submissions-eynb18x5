import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bag = []
        heapq.heapify(bag)
        for num in nums:
            topElement = None
            if len(bag) >= k:
                topElement = bag[0]
                heapq.heappop(bag)
            if topElement:
                heapq.heappush(bag, max(num, topElement))
            else:
                heapq.heappush(bag, num)

        return bag[0]
        
        