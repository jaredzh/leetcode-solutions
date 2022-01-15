class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
        q = deque([(0,0)])
        visited, visited_group = set(), set()
        
        while q:
            steps, i = q.popleft()
            if i == len(arr)-1:
                return steps
            
            for j in [i-1, i+1]:
                if j not in visited and (0<=j<len(arr)):
                    visited.add(j)
                    q.append((steps+1, j))
            
            if arr[i] not in visited_group:
                for j in d[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        q.append((steps+1, j))
                visited_group.add(arr[i])