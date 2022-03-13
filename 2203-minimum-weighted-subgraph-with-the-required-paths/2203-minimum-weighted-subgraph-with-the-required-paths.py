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
        def helper(n, src, graph):
            dist = []
            res = [float("inf")]*n
            for i in range(n):
                if i == src:
                    dist.append((0, i))
                else:
                    dist.append((float("inf"), i))
            heapq.heapify(dist)
            seen = set()
            while True: 
                if not dist:
                    break
                k = heapq.heappop(dist)
                if k[1] in seen:
                    continue
                seen.add(k[1])
                
                res[k[1]] = min(res[k[1]], k[0])
                
                for node, w in graph[k[1]]:
                    #weight = min(dist[node], k[0]+w)
                    heapq.heappush(dist, (k[0]+w, node))
            return res
        l1 = helper(n, src1, G)
        l2 = helper(n, src2, G)
        l3 = helper(n, dest, reverse_G)
        res = float("inf")
        for i, j, k in zip(l1, l2, l3):
            res = min(res, i+j+k)
        return res if res != float("inf") else -1
        