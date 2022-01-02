class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        res = 0
        for t in time:
            d[t%60] += 1
        
        res += ( (d[0]-1) * d[0])/2
        res += ( (d[30]-1) * d[30])/2
        for i in range(1,30):
            res += d[i]*d[60-i]
        
        return res