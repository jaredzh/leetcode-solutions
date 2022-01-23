class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        d = Counter(barcodes).most_common()[::-1]
        n = len(barcodes)
        res = [0]*n
        l = [val for val, ct in d for _ in range(ct)]
        for i in range(0, n, 2):
            res[i] = l.pop()
        for i in range(1, n, 2):
            res[i] = l.pop()
        return res