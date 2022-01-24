class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_str = str(n)
        l = []
        k = 0
        for i in n_str[::-1]:
            if k and not k%3:
                l += ["."]
            l += [i]
            k += 1
        return "".join(l)[::-1]