class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factors = [2, 3, 5]

        for i in prime_factors:
            while n > 1 and n % i == 0:
                n = n // i

        if n == 1:
            return True

        return False  
