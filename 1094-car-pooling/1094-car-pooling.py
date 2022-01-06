class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        l = []
        for n, f, t in trips:
            l.append([f, n])
            l.append([t, -n])
        k = 0
        l.sort()
        for val in l:
            k += val[1]
            if k > capacity:
                return False
        return True