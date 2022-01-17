class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        res = 0
        while target != 1:
            if not maxDoubles:
                return res+target-1
            elif target%2:
                target -= 1
            else:
                target /= 2
                maxDoubles -= 1
            res += 1
        return res