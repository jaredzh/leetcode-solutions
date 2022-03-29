class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        
        @lru_cache(None)
        def dp(day):
            if day > 365:
                return 0
            elif day in days_set:
                return min(dp(day+1)+costs[0], 
                           dp(day+7)+costs[1], 
                           dp(day+30)+costs[2])
            else:
                return dp(day+1)
        return dp(days[0])