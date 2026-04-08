class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxNum = nums[0]
        minNum = nums[0]

        for num in nums:
            maxNum = max(maxNum, num)
            minNum = min(minNum, num)
        
        buckets = [0] * (maxNum - minNum + 1)

        for num in nums:
            buckets[num - minNum] += 1
        
        maxLength = 0
        length = 0

        for bucket in buckets:
            if bucket != 0:
                length += 1
            if bucket == 0:
                maxLength = max(maxLength, length)
                length = 0
        return max(maxLength, length)
        