class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes = []
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if len(indexes) == 0 or temperatures[indexes[len(indexes) - 1]] > temp:
                indexes.append(idx)
            else:
                while len(indexes) > 0 and temperatures[indexes[len(indexes) - 1]] < temp:
                    removedIdx = indexes.pop()
                    result[removedIdx] = idx - removedIdx
                indexes.append(idx)

        return result 


