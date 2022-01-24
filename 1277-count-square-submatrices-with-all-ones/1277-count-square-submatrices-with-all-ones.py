class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i>0 and j>0 and matrix[i][j]:
                    k1, k2, k3 = matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]
                    if matrix[i][j] and k1 and k2 and k3:
                        matrix[i][j] = 1 + min(matrix[i-1][j-1], k1, k2, k3)
        res = 0
        for row in matrix:
            res += sum(row)
        return res