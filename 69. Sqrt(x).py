def mySqrt(x: int) -> int:
        if x <= 1:
            return x

        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            square = mid*mid
            # print(low, high, mid, square)
            
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return low - 1
