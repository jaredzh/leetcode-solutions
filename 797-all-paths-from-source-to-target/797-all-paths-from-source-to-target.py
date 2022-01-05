class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, cur):
            if cur == len(graph)-1:
                res.append(path+[cur])
            for i in graph[cur]:
                dfs(path+[cur], i)
        dfs([],0)
        return res
                