class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        start, tank = 0, 0
        for i in range(n):
            tank += gas[i]-cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        return start