class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = []
        for i in range(1, 10):
            num = i
            nextDigit = i+1

            while num<= high and nextDigit<=9:
                num = num*10 + nextDigit
                if low<=num and num<= high:
                    arr.append(num)
                nextDigit += 1
            
        arr.sort()
        return arr


