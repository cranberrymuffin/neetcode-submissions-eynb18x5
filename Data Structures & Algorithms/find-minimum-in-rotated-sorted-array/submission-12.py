class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinH(nums, 0, len(nums) - 1)
    
    def findMinH(self, nums: List[int], start: int, end: int) -> int:
        middleIdx = (start + end) // 2

        if nums[middleIdx] <= nums[middleIdx-1]:
            return nums[middleIdx]
        elif nums[end] < nums[start] and nums[middleIdx] > nums[end]:
            return self.findMinH(nums, middleIdx + 1, end)
        else:
            return self.findMinH(nums, start, middleIdx - 1) 


        