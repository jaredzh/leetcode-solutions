class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(int)
        res = float("inf")
        for i, v in enumerate(cards):
            if v in d:  
                res = min(res, i-d[v]+1)
            d[v] = i
        
        return res if res < float("inf") else -1
