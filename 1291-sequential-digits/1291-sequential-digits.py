class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        for digit in range(1, 9):
            num = nxt = digit
            while num <= high and nxt < 10:
                if num >= low:
                    res += [num]
                nxt += 1
                num = num *10 + nxt
        return sorted(res)