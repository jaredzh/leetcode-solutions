class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        s = set()
        d = defaultdict(list)
        for t in trust:
            s.add(t[0])
            d[t[1]].append(t[0])
        
        for i in range(1, n+1):
            if i not in s and len(d[i]) == n-1:
                return i
        return -1