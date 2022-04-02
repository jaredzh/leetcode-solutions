class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        
        while left < right:
            if s[left] != s[right]:
                s1, s2 = s[left:right], s[left+1:right+1]
                return s1 == s1[::-1] or s2 == s2[::-1]
            else:
                left, right = left + 1, right - 1
        return True
            