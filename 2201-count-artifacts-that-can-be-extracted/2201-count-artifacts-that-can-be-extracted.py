class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        res = 0
        dig_s = set()
        for i,j in dig:
            dig_s.add((i,j))
        for a in artifacts:
            topleft = a[0:2]
            botright = a[2:]
            excavated = True
            for i in range(topleft[0], botright[0]+1):
                for j in range(topleft[1], botright[1]+1):
                    if (i,j) not in dig_s:
                        excavated = False
            if excavated:
                res += 1
        return res
        