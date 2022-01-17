class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
        for i in range(0, n-n%k-k+1, k):
            res.append(s[i:i+k])
        if n%k:
            tmp = s[n-n%k:]
            while len(tmp) < k:
                tmp += fill
            res.append(tmp)
        return res