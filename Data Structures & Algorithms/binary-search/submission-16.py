class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)
    def binary_search(self, nums, start, end, target) -> int:
        if start > end:
            return -1
        middle = start + ((end - end) // 2)
        if nums[middle] == target:
            return middle
        
        if nums[middle] > target:
            return self.binary_search(nums, start, middle -1, target)
        else:
            return self.binary_search(nums, middle + 1, end, target)
