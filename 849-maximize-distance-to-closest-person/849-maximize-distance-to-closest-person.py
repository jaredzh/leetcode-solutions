class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        ones = []
        for i, v in enumerate(seats):
            if v == 1:
                ones.append(i)
        res = 0
        for i in range(len(ones)-1):
            res = max(res, (ones[i+1]-ones[i])//2)
        return max(res, ones[0], n-ones[-1]-1)
        