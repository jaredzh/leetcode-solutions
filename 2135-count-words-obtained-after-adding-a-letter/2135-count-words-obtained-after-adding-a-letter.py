class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        start = set(["".join(sorted(w)) for w in startWords])
        res = 0
        for tar in targetWords:
            word = "".join(sorted(tar))
            for i in range(len(word)):
                if word[:i]+word[i+1:] in start:
                    res += 1
                    break
        return res
       
        