class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        prefix = [0] + list(itertools.accumulate(nums))
        
        @lru_cache(None)
        def solve(curr_i, k):
            if k == 1:
                return prefix[n] - prefix[curr_i]
            
            res = prefix[n]
            for i in range(curr_i, n-k+1):
                left_sum = prefix[i+1] - prefix[curr_i]   
                
                if left_sum >= res:
                    break
                    
                right_sum = solve(i+1, k-1)
                res = min(res, max(left_sum, right_sum))
                
            return res
        
        return solve(0, m)