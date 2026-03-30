class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        i = 0
        k = len(heights) - 1

        for i in range(0,len(heights)):
            for k in range(len(heights) - 1, i, -1):
                maxVolume = max(maxVolume, min(heights[i], heights[k]) * (k - i))
        return maxVolume
    

        