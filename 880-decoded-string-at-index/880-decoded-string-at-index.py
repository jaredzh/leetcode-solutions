class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for val in s:
            if val.isdigit():
                size *= int(val)
            else:
                size += 1
        
        for val in reversed(s):
            k %= size
            if not k and val.isalpha():
                return val
            if val.isdigit():
                size /= int(val)
            else:
                size -= 1