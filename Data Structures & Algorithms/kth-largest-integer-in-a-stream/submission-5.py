import heapq

class KthLargest:
    h = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        toPush = val
        if len(self.h) >= self.k:
            toPush = max(toPush, heapq.heappop(self.h))
        heapq.heappush(self.h, toPush)
        return self.h[0]