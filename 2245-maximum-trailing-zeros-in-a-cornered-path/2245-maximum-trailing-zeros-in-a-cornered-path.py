class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hori = [[0, 0]*n for _ in range(m)]
        vert = [[0, 0]*n for _ in range(m)]
        
        def f(x, base):
            ret = 0
            while not x % base:
                ret += 1
                x = x//base
            return ret
                
        for i in range(m):
            two_ct, five_ct = 0, 0
            for j in range(n):
                val = grid[i][j]
                two_ct += f(val, 2)
                five_ct += f(val, 5)
                hori[i][j] = [two_ct, five_ct]
        
        for j in range(n):
            two_ct, five_ct = 0, 0
            for i in range(m):
                val = grid[i][j]
                two_ct += f(val, 2)
                five_ct += f(val, 5)
                vert[i][j] = [two_ct, five_ct]
        
        res = 0
        for i in range(m):
            for j in range(n):
                # left up
                twos = hori[i][j][0] + vert[i][j][0]
                fives = hori[i][j][1] + vert[i][j][1]
                lu = min(twos - f(grid[i][j], 2) , fives - f(grid[i][j], 5))
                
                # left down
                twos = hori[i][j][0]
                twos += ( vert[m-1][j][0] - vert[i-1][j][0] if i > 0 else vert[m-1][j][0])
                fives = hori[i][j][1]
                fives += ( vert[m-1][j][1] - vert[i-1][j][1] if i > 0 else vert[m-1][j][1])
                ld = min(twos - f(grid[i][j], 2) , fives - f(grid[i][j], 5))
                
                # right up
                twos = vert[i][j][0]
                twos += ( hori[i][n-1][0] - hori[i][j-1][0] if j > 0 else hori[i][n-1][0]) 
                fives = vert[i][j][1]
                fives += ( hori[i][n-1][1] - hori[i][j-1][1] if j > 0 else hori[i][n-1][1] )
                ru = min(twos - f(grid[i][j], 2) , fives - f(grid[i][j], 5))
                
                # right down
                twos, fives = 0, 0
                twos += ( vert[m-1][j][0] - vert[i-1][j][0] if i > 0 else vert[m-1][j][0])
                twos += ( hori[i][n-1][0] - hori[i][j-1][0] if j > 0 else hori[i][n-1][0] )
                fives += ( vert[m-1][j][1] - vert[i-1][j][1] if i > 0 else vert[m-1][j][1])
                fives += ( hori[i][n-1][1] - hori[i][j-1][1] if j > 0 else hori[i][n-1][1] )
                rd = min(twos - f(grid[i][j], 2) , fives - f(grid[i][j], 5))
                
                res = max(res, max([lu, ld, ru, rd]))
                
        return res
        