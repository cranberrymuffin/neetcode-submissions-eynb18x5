class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            pair = target - num
            try:
                pairIdx = nums.index(pair, idx + 1)
                return [idx, pairIdx]
            except ValueError:
                continue
