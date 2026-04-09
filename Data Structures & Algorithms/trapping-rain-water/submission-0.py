class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0

        trapped = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if maxL < maxR:
                l += 1
                trapped += max(0, min(maxL, maxR) - height[l])
            else:
                r -= 1
                trapped += max(0, min(maxL, maxR) - height[r])
        
        return trapped
