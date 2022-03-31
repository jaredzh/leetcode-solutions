class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = defaultdict(int)
        for i, val in enumerate(s):
            last_occ[val] = i
        
        left, n, res = 0, len(s), []
        while left < n:
            k, right = 0, last_occ[s[left]]
            while left <= right:
                right = max(right, last_occ[s[left]])
                left, k = left + 1, k + 1
            res.append(k)
        return res