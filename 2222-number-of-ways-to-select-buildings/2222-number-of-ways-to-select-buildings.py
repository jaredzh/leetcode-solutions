class Solution:
    def numberOfWays(self, s: str) -> int:
        pre_zeros = []
        pre_ones = []
        k1, k2 = 0, 0
        for val in s:
            pre_zeros.append(k1)
            pre_ones.append(k2)
            if val == "0":
                k1 += 1
            else:
                k2 += 1
        
        post_zeros, post_ones = [0]*len(s), [0]*len(s)
        k1, k2 = 0, 0
        for i in range(len(s)-1, -1, -1):
            post_zeros[i] = k1
            post_ones[i] = k2
            if s[i] == "0":
                k1 += 1
            else:
                k2 += 1
        
        res = 0
        for i, val in enumerate(s):
            if val == "0":
                res += (pre_ones[i]*post_ones[i])
            else:
                res += (pre_zeros[i]*post_zeros[i])
        return res