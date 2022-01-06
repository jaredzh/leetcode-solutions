class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.res = False
        def validate(l):
            for i in range(len(l)-1):
                n1 = l[i].lstrip('0')
                n2 = l[i+1].lstrip('0')
    
                if not n1:
                    return False
                if not n2:
                    n2 = 0
                    
                n1 = int(n1)
                n2 = int(n2)
                if n1 != n2+1 or not n1 > n2:
                    return False
            return True
        def dfs(s_in, path):
            if not s_in:
                if len(path) > 1:
                    self.res = True 
                return
            for i in range(len(s_in)+1):
                if validate(path+[s_in[:i+1]]):
                    dfs(s_in[i+1:], path+[s_in[:i+1]])
        dfs(s, [])
        return self.res
                