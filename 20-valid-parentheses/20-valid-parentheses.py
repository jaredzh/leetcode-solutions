class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for c in s:
            if c == "(" or c=="{" or c=="[":
                l.append(c)
            else:
                if not l:
                    return False
                k = l.pop()
                if k == "(" and c != ")" or \
                    k == "{" and c != "}" or k == "[" and c != "]": 
                    return False
        return True if not l else False
        