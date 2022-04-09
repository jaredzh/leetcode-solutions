class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [[-val, key] for key, val in Counter(nums).items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]