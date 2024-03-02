def canPlaceFlowers(flowerbed, n):
        l = len(flowerbed)
        count = 0
        
        i = 1
        while i > 0 and i+2 < l:
            if flowerbed[i] + flowerbed[i+1] + flowerbed[i+2] == 0:
                count = count + 1
                i = i + 2
            else:
                i = i + 1
        
        i = 0
        if flowerbed[i] + flowerbed[i+1] == 0:
            count = count + 1
            
        i = l - 2
        if flowerbed[i] + flowerbed[i+1] == 0:
            count = count + 1
        
        # return count == n
        return count
