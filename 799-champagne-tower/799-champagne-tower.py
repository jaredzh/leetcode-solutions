class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = defaultdict(int)
        dp[(0,0)] = poured
        for i in range(0, query_row+1):
            for j in range(0, i+1):
                if dp[(i,j)] > 1:
                    k = (dp[(i,j)]-1)/2.0
                    dp[(i+1,j)] += k
                    dp[(i+1, j+1)] += k
                    dp[(i,j)] = 1
        return dp[(query_row, query_glass)]
    