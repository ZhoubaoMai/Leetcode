class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        firFlower, secFlower = None, None
        count = 0
        for index, num in enumerate(flowerbed):
            if num:
                if firFlower == None:
                    firFlower, secFlower = index, index
                    count = int((index)/2) if index > 1 else count
                elif secFlower == firFlower:
                    secFlower = index
                    count += int((secFlower-firFlower-2)/2)
                else:
                    firFlower, secFlower = secFlower, index
                    count += int((secFlower-firFlower-2)/2)
                if count >= n:
                    return True
        if firFlower == None:
            count = int((len(flowerbed)+1)/2)
        else:
            count = count + int((len(flowerbed)-secFlower-1)/2) if secFlower < len(flowerbed)-2 else count
        return count >= n
