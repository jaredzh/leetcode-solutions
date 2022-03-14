class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def topo_sort(n, G):
            res, indegree = [], [0]*n
            import queue
            que = queue.Queue()
            for i in range(n):
                for j in G[i]:
                    indegree[j] += 1

            for i in range(n):
                if indegree[i] == 0:
                    que.put(i)

            while not que.empty():
                curr = que.get()
                res.append(curr)
                for j in G[curr]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        que.put(j)
            return res
        
        d = defaultdict(list)
        for prereq in prerequisites:
            d[prereq[0]].append(prereq[-1])
        return len(topo_sort(numCourses, d)) == numCourses