class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        G = defaultdict(list)
        reverse_G = defaultdict(list)
        for e in edges:
            G[e[0]].append(e[1:])
            reverse_G[e[1]].append([e[0], e[2]])
        def f(n, src, graph):
            dist = []
            res = [float("inf")]*n
            for i in range(n):
                dist.append((0, i) if i == src else (float("inf"), i))
            heapq.heapify(dist)
            seen = set()
            while True: 
                if not dist:
                    break
                curr_w, curr = heapq.heappop(dist)
                if curr in seen:
                    continue
                seen.add(curr)     
                res[curr] = min(res[curr], curr_w)     
                for node, w in graph[curr]:
                    heapq.heappush(dist, (curr_w+w, node))
            return res
        res = float("inf")
        for i, j, k in zip(f(n, src1, G), f(n, src2, G), f(n, dest, reverse_G)):
            res = min(res, i+j+k)
        return res if res != float("inf") else -1
        