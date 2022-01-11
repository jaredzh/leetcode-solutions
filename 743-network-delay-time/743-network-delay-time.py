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
            G[u].append([v, w])
        dist = {node:float("inf") for node in range(1, n+1)}
        seen = set()
        dist[k] = 0
        
        while True:
            cur_cand = -1
            cur_w = float("inf")
            for node, w in dist.items():
                if node not in seen and w < cur_w:
                    cur_cand = node
                    cur_w = w
            
            if cur_cand < 0:
                break
            seen.add(cur_cand)
            for node, d in G[cur_cand]:
                dist[node] = min(dist[node], dist[cur_cand]+d)
        
        ans = max(dist.values())
        return ans if ans < float('inf') else -1