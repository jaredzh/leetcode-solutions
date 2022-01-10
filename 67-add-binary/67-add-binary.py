class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = []
        i, j = len(a)-1, len(b)-1
        while i>=0 and j>=0:
            tmp = int(a[i])+int(b[j])+carry
            carry = tmp//2
            res.append(str(tmp%2))
            i -= 1
            j -= 1
        while i >= 0:
            tmp = int(a[i])+carry
            carry = tmp//2
            res.append(str(tmp%2))
            i -= 1
        while j >= 0:
            tmp = int(b[j])+carry
            carry = tmp//2
            res.append(str(tmp%2))
            j -= 1
        if carry:
            res+=["1"]
        
        return "".join(res)[::-1]