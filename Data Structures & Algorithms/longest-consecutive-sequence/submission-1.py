class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        all_nums = set(nums)

        for num in nums:
            if num - 1 not in all_nums:
                length = 0
                curr = num
                while curr in all_nums:
                    length += 1
                    curr += 1

                longest = max(longest, length)


        return longest
        