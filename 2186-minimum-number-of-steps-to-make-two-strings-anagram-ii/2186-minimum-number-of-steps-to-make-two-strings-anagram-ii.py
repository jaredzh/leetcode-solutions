class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_d, t_d = Counter(s), Counter(t)
        res = 0
        for k, v in s_d.items():
            if k not in t_d:
                res += v
            elif v > t_d[k]:
                res += v-t_d[k]
        
        for k, v in t_d.items():
            if k not in s_d:
                res += v
            elif v > s_d[k]:
                res += v-s_d[k]
        return res