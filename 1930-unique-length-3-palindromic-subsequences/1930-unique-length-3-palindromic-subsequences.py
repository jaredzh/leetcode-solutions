class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        res = 0
        for left, v in enumerate(s):
            if v not in seen:
                seen.add(v)
                right = 0
                for j in range(left+1, len(s)):
                    if s[j] == v:
                        right = j
                if not right:
                    continue
                res += len(set(s[left+1:right]))
        return res