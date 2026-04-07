class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums_idx:
                result = [i, nums_idx[pair]]
                result.sort()
                return result
            nums_idx[num] = i
            
        