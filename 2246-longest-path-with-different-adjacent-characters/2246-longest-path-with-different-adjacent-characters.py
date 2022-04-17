class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        G = defaultdict(list)
        for i, v in enumerate(parent):
            if i == 0:
                continue
            G[v].append(i)
            
        @lru_cache(None)
        def dfs(node):
            if node not in G:
                return 1
            res = 1
            for child in G[node]:
                if s[child] != s[node]:
                    res = max(res, dfs(child)+1)
            return res
            
        if len(parent) == 1:
            return 1
        ret = 0
        for parent in G:
            candi = []
            for child in G[parent]:
                if s[parent] != s[child]:
                    candi.append(dfs(child))
            ret = max(ret, sum(nlargest(2, candi))+1)
            
        return ret
                
            