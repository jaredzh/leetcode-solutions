class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        n1, n2 = len(pattern), len(words)
        if n1 != n2:
            return False
        d = {}
        seen = set()
        for i in range(n1):
            if pattern[i] not in d:
                if words[i] in seen:
                    return False
                d[pattern[i]] = words[i]
                seen.add(words[i])
            elif d[pattern[i]] != words[i]:
                return False
        return True