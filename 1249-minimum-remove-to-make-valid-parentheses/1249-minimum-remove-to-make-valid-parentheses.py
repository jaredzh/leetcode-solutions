class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        remove = set()
        k = 0
        for i, c in enumerate(s):
            if c == "(":
                k += 1
            elif c == ")":
                k -= 1
            if k < 0:
                remove.add(i)
                k += 1
        k = 0
        for i, c in enumerate(s[::-1]):
            if c == ")":
                k += 1
            elif c == "(":
                k -= 1
            if k < 0:
                remove.add(len(s) - i - 1)
                k += 1
        res = ""
        for i, c in enumerate(s):
            if i not in remove:
                res += c
        return res
        