import math
import heapq

class Solution:
    def distanceToOrigin(self, point: List[int]) -> int:
        x1 = 0
        y1 = 0
        x2 = point[0]
        y2 = point[1]
        return math.sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            dist = self.distanceToOrigin(point)
            point_to_push = point
            if len(h) >= k:
                (dist2, point2) = heapq.heappop(h)
                if -dist2 < dist:
                    point_to_push = point2
                    dist = -dist2
            heapq.heappush(h, (-dist, point_to_push))
        
        return list(map(lambda data: data[1], h))

        