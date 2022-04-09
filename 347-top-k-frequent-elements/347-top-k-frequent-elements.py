class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        for key, val in d.items():
            heap.append([-val, key])
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]