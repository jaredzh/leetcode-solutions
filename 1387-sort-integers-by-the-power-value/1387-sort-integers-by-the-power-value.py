class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def power(n):
            t = 0
            while n != 1:
                if n%2:
                    n = 3*n + 1
                else:
                    n /= 2
                t += 1
            return t
        
        l = []
        for i in range(lo, hi+1):
            l.append((power(i), i))
        l.sort()
        return l[k-1][1]