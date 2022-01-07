class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        res = 0
        for i, v in enumerate(s):
            if v not in seen:
                seen.add(v)
                right = -1
                for j in range(i+1, len(s)):
                    if s[j] == v:
                        right = j
                if right == -1:
                    continue
                res += len(set(s[i+1:right]))
        return res