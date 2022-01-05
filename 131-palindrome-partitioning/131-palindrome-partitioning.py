class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        def palin(s_in):
            return s_in == s_in[::-1]
        
        def dfs(s, path):
            if not s:
                res.append(path[:])
            for i in range(1, len(s)+1):
                if palin(s[:i]):
                    dfs(s[i:], path+[s[:i]])
           
        dfs(s, [])
        return res
    