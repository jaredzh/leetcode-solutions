class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)    
        seen = set()
        def dfs(src, dst):
            if src in seen:
                return False
            seen.add(src)
            if src == dst:
                return True
            for node in graph[src]:
                if dfs(node, dst):
                    return True
            return False
        
        for s, d in edges:
            seen = set()
            if s in graph and d in graph and dfs(s, d):
                return [s,d]
            graph[s].add(d)
            graph[d].add(s)