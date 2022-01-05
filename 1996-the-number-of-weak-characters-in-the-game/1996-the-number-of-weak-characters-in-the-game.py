class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (-x[0], x[1]))
        res = 0
        max_d = 0
        max_a = properties[-1][0]
        print(properties)
        for a, d in properties:
            if d < max_d:
                res += 1
            max_d = max(max_d, d)
        return res