class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        l = text.split()
        l[0] = l[0].lower()
        res = " ".join(sorted(l, key=lambda x:len(x)))
        return res[0].upper() + res[1:]