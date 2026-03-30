class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0

        i = 0
        j = len(heights) - 1
        
        while i != j:
            maxVolume = max(min(heights[i], heights[j]) * (j - i), maxVolume)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxVolume

        