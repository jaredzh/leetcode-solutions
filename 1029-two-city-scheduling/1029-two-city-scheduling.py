class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n_2 = len(costs)//2
        costs.sort(key=lambda x: abs(x[1]-x[0]))
        res, A, B = 0, 0, 0
        
        for a_cost, b_cost in reversed(costs):
            if A == n_2:
                res += b_cost
                B += 1
            elif B == n_2:
                res += a_cost
                A += 1
            elif a_cost < b_cost:
                res += a_cost
                A += 1
            else:
                res += b_cost
                B += 1
        return res