class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        d = defaultdict(int)
        for i in range(len(s)-minSize+1):
            s1 = s[i:i+minSize]
            if s1 in d or len(set(s1)) <= maxLetters:
                d[s1] += 1
        if not d:
            return 0
        return max(d.values())