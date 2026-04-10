class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prev = 1
        for i, num in enumerate(nums):
            prefix[i] *= prev
            prev *= num

        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] *= prev
            prev *= nums[i]

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result