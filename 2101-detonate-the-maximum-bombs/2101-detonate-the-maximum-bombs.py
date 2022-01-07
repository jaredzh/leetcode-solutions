class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        res = 0
        n, G = len(bombs), defaultdict(list)
        
        def intersect(b1, b2):
            x1, y1, r1 = b1
            x2, y2, r2 = b2
            dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
            if dist <= (r1):
                return True
            return False
        
        for i in range(n):
            for j in range(n):
                if i != j and intersect(bombs[i], bombs[j]):
                    G[i].append(j)
        def dfs(visited, node):
            for child in G[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(visited, child)
            return len(visited)
        
        for i in range(n):
            res = max(res, dfs(set([i]), i))
        
        return res
                