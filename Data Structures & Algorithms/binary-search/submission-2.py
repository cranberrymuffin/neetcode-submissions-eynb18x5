class Solution:
    def mid(self, start, end):
        return int((start + end) / 2)
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        mid = self.mid(start,end)
        while(mid >=0 and mid <len(nums) and start <= end):
            if(nums[mid] == target):
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            mid = self.mid(start,end)

        return -1


        