class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinH(nums, 0, len(nums) - 1)
    
    def findMinH(self, nums: List[int], start: int, end: int) -> int:
        middleIdx = (start + end) // 2

        if nums[middleIdx] <= nums[middleIdx-1]:
            return middleIdx
        elif nums[end] < nums[start] and nums[middleIdx] > nums[end]:
            return self.findMinH(nums, middleIdx + 1, end)
        else:
            return self.findMinH(nums, start, middleIdx - 1) 

    def search(self, nums: List[int], target: int) -> int:
        pivotIdx = self.findMin(nums)

        if nums[len(nums) - 1] < target:
            start = 0
            end = pivotIdx - 1
        else:
            start = pivotIdx
            end = len(nums) - 1

        
        while start <= end:
            middleIdx = (start + end) // 2
            print(start)
            print(end)
            print(middleIdx)
            if nums[middleIdx] == target:
                return middleIdx
            elif nums[middleIdx] > target:
                end = middleIdx - 1
            else:
                start = middleIdx + 1


        return -1
        