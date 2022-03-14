class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def topo_sort(n, G):
            res, indegree = [], [0]*n
            dq = deque()
            for i in range(n):
                for j in G[i]:
                    indegree[j] += 1

            for i in range(n):
                if indegree[i] == 0:
                    dq.append(i)

            while dq:
                curr = dq.popleft()
                res.append(curr)
                for j in G[curr]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        dq.append(j)
            return res
        
        d = defaultdict(list)
        for a, b in prerequisites:
            d[b].append(a)
        l = topo_sort(numCourses, d)
        return l if len(l)==numCourses else []