import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            distance = -1 * (math.sqrt((0 - x)**2 + (0 - y)**2))
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (distance, x, y))
            else:
                heapq.heappush(maxHeap, (distance, x, y))
                heapq.heappop(maxHeap)
        
        return [[x,y] for distance,x,y in maxHeap]