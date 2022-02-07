class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = Counter(s)
        for c in t:
            if c not in d or not d[c]:
                return c
            d[c] -= 1
        