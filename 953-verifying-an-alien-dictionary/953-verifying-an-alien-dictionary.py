class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = defaultdict(int)
        for i, v in enumerate(order):
            d[v]=i
        
        def leq(w1, w2):
            if w1 == w2:
                return True
            n = min(len(w1), len(w2))
            for i in range(n):
                if d[w1[i]] > d[w2[i]]:
                    return False
                if d[w1[i]] < d[w2[i]]:
                    return True
            return len(w1) <= len(w2)
        
        for i in range(len(words)-1):
            if not leq(words[i], words[i+1]):
                return False
        return True