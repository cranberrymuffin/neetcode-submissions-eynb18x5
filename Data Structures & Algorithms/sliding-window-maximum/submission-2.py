from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        windowStart = 0
        windowEnd = k
        maxes = []
        for idx, num in enumerate(nums):
            if idx >= windowEnd:
                windowStart += 1
                windowEnd += 1
                maxes.append(nums[dq[0]])
            while len(dq) > 0 and (dq[0] < windowStart or nums[dq[0]] < num):
                dq.popleft()
            while len(dq) > 0 and nums[dq[len(dq) - 1]] < num:
                dq.pop()
            dq.append(idx)

        maxes.append(nums[dq[0]])
        return maxes
            
            

            