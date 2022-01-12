class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        d = {}
        for o in order:
            d[o] = 0
        str2 = ""
        for val in s:
            if val not in d:
                str2 += val
            else:
                d[val] += 1
        str1 = ""
        for k in order:
            str1 += (d[k]*k)
        return str1+str2