class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while(start < end):
            sum_val = numbers[start] + numbers[end]
            if sum_val == target:
                return [start + 1, end + 1]
            if sum_val > target:
                end -= 1
            if sum_val < target:
                start += 1
        
        