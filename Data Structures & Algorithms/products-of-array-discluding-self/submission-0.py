from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 0.0001
        product = reduce(lambda x, y: x * y, nums)
        for i in range(len(nums)):
            nums[i] = int(product/nums[i])
        return nums

        