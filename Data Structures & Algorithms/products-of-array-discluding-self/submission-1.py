class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        product = 1
        for i, num in enumerate(nums):
            prefix[i] = product
            product *= num
        print(prefix)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = product
            product *= nums[i]
        print([postfix])

        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])

        return result