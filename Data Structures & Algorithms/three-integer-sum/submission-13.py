class Solution:
    def twoSum(self, nums: List[int], target: int, idx: int) -> int:
        results = []
        for i, num in enumerate(nums):
            if i == idx:
                continue
            try:
                pair = nums.index(target - num, i + 1)
                if pair == idx:
                    continue
                result = sorted([num, nums[pair]])
                if result not in results:
                    results.append(result)

            except ValueError:
                continue
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for idx, num in enumerate(nums):
            pairs = self.twoSum(nums, -num, idx)
            for pair in pairs:
                result = sorted([num] + pair)
                if result not in results:
                    results.append(result)

        return results
                
