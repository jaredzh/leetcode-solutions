class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for n in arr:
            diff = -abs(n-x)
            if len(pq) < k:
                heapq.heappush(pq, [diff, n])
            else:
                if pq[0][0] != diff:
                    heapq.heappushpop(pq, [diff, n])
        return [val for _, val in sorted(pq, key=lambda x:x[1])]