class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        G = defaultdict(list)
        for u, v, w in times:
            G[u].append([w, v])
        dist = {node:float("inf") for node in range(1, n+1)}
        
        def dfs(node, curr_w):
            if curr_w >= dist[node]:
                return
            dist[node] = curr_w
            for w, n in sorted(G[node]):
                dfs(n, curr_w+w)
        
        dfs(k, 0)
        res = max(dist.values())
        if not res < float("inf"):
            return -1
        return res
            