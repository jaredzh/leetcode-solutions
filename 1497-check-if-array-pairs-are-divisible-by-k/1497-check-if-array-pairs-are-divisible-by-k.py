class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        d = defaultdict(list)
        for v in arr:
            d[v%k].append(v)
            
        for key, value in d.items():
            comp = -key%k
            if not comp and len(value)%2:
                return False
            elif comp not in d or len(value) != len(d[comp]):
                return False
        return True