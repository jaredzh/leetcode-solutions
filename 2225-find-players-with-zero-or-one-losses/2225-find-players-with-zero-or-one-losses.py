class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] += 1
        res = [sorted([key for key, val in losses.items() if val == 0]),
               sorted([key for key, val in losses.items() if val == 1])]
        return res