class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []
        for i in range(len(heights)-1):
            dif = heights[i+1] - heights[i]
            if dif > 0:
                heapq.heappush(heap, dif)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i
        return len(heights)-1