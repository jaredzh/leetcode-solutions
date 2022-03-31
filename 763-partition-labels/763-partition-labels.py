class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = defaultdict(int)
        for i, val in enumerate(s):
            last_occ[val] = i
        
        left = 0
        n = len(s)
        res = []
        while left < n:
            right = last_occ[s[left]]
            k = 0
            while left <= right:
                right = max(right, last_occ[s[left]])
                left += 1
                k += 1
            res.append(k)
        return res