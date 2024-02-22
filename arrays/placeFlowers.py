class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zeroCounter = 0
        if len(flowerbed) == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                zeroCounter = 0
                continue
            if flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    zeroCounter+=1
                    continue
            if flowerbed[i + 1] == 1:
                if zeroCounter > n:
                    return True

        return False