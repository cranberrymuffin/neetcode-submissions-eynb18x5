class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        
        last = 1
        for num in nums:
            prefix.append(last)
            last = prefix[len(prefix) - 1] * num
        
        last = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix = [last ] + suffix
            last = suffix[0] * nums[i]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

