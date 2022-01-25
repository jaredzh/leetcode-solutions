class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        self.res = 0
        self.diff = float("inf")
        def dfs(k, i):
            if abs(target-k) < self.diff:
                self.diff = abs(target-k)
                self.res = k
            if abs(target-k) == self.diff and k < target:
                self.res = k
            if i == len(toppingCosts):
                return
            v = toppingCosts[i]
            dfs(k, i+1)
            dfs(k+v, i+1)
            dfs(k+2*v, i+1)
                
        for base in baseCosts:
            dfs(base, 0)
        return self.res
        
                