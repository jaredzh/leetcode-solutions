class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res = []
        res.append(s[0:spaces[0]])
        for i in range(1, len(spaces)):
            res.append(s[spaces[i-1]:spaces[i]])
        res.append(s[spaces[-1]:])
        return " ".join(res)