class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        i = 0
        res = []
        k = len(p)
        s_d = Counter(s[:k])
        p_d = Counter(p)
        if s_d == p_d:
            res.append(0)
        for i in range(k, len(s)):
            if s[i] in s_d:
                s_d[s[i]] += 1
            else:
                s_d[s[i]] = 1
            s_d[s[i-k]] -= 1
            if not s_d[s[i-k]]:
                del s_d[s[i-k]]
            if s_d == p_d:
                res.append(i-k+1)
        return res