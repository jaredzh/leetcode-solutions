class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "R":
                count += 1
            else:
                count -= 1
            if not count:
                res += 1
        return res