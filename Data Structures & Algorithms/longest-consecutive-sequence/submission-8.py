class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        buckets = [0] * (max(nums) - min(nums) + 1)

        for num in nums:
            buckets[num - min(nums)] += 1
        
        longest = 0

        length = 0
        for bucket in buckets:
            if bucket == 0:
                longest = max(longest, length)
                length = 0
            else:
                length += 1
        
        return  max(longest, length)


        