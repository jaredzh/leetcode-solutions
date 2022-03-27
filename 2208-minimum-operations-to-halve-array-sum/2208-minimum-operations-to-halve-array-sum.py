class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = float(sum(nums))
        tar = tot / 2
        res = 0
        heap = []
        for n in nums:
            heapq.heappush(heap, -float(n))
        while tot > tar:
            curr = heapq.heappop(heap)
            tot += (curr/2.0)
            heapq.heappush(heap, curr/2.0)
            res += 1
        return res
        