class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        d = Counter(barcodes).most_common()
        n = len(barcodes)
        res = [0]*n
        l = [val for val, ct in d for _ in range(ct)]
        print(l)
        for i in range(0, n, 2):
            res[i] = l.pop(0)
        for i in range(1, n, 2):
            res[i] = l.pop(0)
        return res