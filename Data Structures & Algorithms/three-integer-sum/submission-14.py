class Solution:
    def twoSum(self, nums: List[int], start:int, target: int) -> List[int]:
        seen = set()
        results = []
        for i in range(start, len(nums)):
            pair = target - nums[i]
            if pair in seen :
                results.append([nums[i], pair])
            else:
                seen.add(nums[i])
        return results


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for idx, num in enumerate(nums):
            pairs = self.twoSum(nums, idx + 1, -num)
            for pair in pairs:
                result = [num] + pair
                result.sort()
                results.add(tuple(result))
        
        return list(map(lambda result: list(result), results))
        