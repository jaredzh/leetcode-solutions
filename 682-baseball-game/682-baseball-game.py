class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l = []
        for o in ops:
            if o == "+":
                l.append(l[-1]+l[-2])
            elif o == "D":
                l.append(l[-1]*2)
            elif o == "C":
                l.pop()
            else:
                l.append(int(o))
        return sum(l)