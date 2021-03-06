class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        for i, m in enumerate(mat):
            heapq.heappush(heap, [m.count(1), i])
        return [heapq.heappop(heap)[1] for i in range(k)]