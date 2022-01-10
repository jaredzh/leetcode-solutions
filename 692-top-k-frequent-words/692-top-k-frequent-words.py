class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        l = []
        d = Counter(words)
        for key, v in d.items():
            l.append((v, key))
        l.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for _, val in l[:k]:
            res += [val]
        return res
        