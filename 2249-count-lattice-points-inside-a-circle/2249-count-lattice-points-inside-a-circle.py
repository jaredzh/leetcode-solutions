class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    dist = math.sqrt((i-x)**2 + (j-y)**2)
                    if dist <= r and (i, j) not in res:
                        res.add((i, j))
        return len(res)