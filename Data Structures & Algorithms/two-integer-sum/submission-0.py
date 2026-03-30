class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        couple = {}
        for i, num in enumerate(nums):
            if(target - num) in couple:
                return [couple[target-num], i]
            else:
                couple[num] = i
            