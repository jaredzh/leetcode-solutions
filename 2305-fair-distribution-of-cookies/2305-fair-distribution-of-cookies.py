class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float("inf")
        self.l = [0] * k
        
        def helper(i):
            if i == len(cookies):
                self.res = min(self.res, max(self.l))
                
            if self.res <= max(self.l):
                return
            for j in range(k):
                self.l[j] += cookies[i]
                helper(i + 1)
                self.l[j] -= cookies[i]
        
        helper(0)
        return self.res