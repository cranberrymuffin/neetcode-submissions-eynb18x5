class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end and start < len(nums) and end >= 0:
            middle = (start + end)//2 + 1
            if nums[middle] == target:
                return middle
            print(nums[start])
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if nums[middle] > target:
                end = middle - 1
            if nums[middle] < target:
                start = middle + 1
        if start < len(nums) and nums[start] == target:
            return start
        if end >= 0 and nums[end] == target:
            return end
        return -1