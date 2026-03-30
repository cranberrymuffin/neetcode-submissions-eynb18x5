class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = [intervals[0]]
        for i, interval in enumerate(intervals):
            last = len(merged) - 1
            curr = merged[last]
            if i==0:
                continue
            if curr[1] >= interval[0]:
                merged[last][0] = min(curr[0], interval[0])
                merged[last][1] = max(curr[1], interval[1])
            else:
                merged.append(interval)
        return merged



        