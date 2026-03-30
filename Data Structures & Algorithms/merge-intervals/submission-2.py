class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = merged[len(merged) - 1]
            if curr[1] >= intervals[i][0]:
                curr[0] = min(intervals[i][0], curr[0])
                curr[1] = max(intervals[i][1], curr[1])
            else:
                merged.append(intervals[i])

        return merged
        