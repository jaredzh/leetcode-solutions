class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            if (flowerbed[0] != 0 and n != 0) or (flowerbed[0] != 1 and n > 1):
                return False
            else:
                return True
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1]==0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == (len(flowerbed)-1):
                if flowerbed[i] == 0 and flowerbed[i-1]==0:
                    n -= 1
                    flowerbed[i] = 1
            elif not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                n -= 1
                flowerbed[i] = 1
        return n == 0