class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        G = defaultdict(list)
        roads = set()
        self.res = 0
        for v1, v2 in connections:
            G[v1].append(v2)
            G[v2].append(v1)
            roads.add((v1, v2))
        
        def dfs(node, parent):
            if (parent, node) in roads:
                self.res += 1
            for child in G[node]:
                if child == parent:
                    continue
                dfs(child, node)
        dfs(0, -1)
        return self.res
    