class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        count1, res1 = 1, 0
        for c in text:
            if c == pattern[1]:
                res1 += count1
            if c == pattern[0]:
                count1 += 1
        
        count2, res2 = 1, 0
        for c in text[::-1]:
            if c == pattern[0]:
                res2 += count2
            if c == pattern[1]:
                count2 += 1
        return max(res1, res2)