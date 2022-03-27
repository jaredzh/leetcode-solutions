class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot, res = 0.0, 0
        heap = []
        for n in nums:
            tot += n
            heapq.heappush(heap, -float(n))
        tar = tot / 2.0
        while tot > tar:
            curr = heapq.heappop(heap)
            tot += (curr/2.0)
            heapq.heappush(heap, curr/2.0)
            res += 1
        return res
        