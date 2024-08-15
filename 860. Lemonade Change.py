class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change1 = 0
        change2 = 0

        if bills[0] != 5:
            return False

        for i in bills:
            if i == 5:
                change1 += 1
            elif i == 10:
                if change1 > 0:
                    change1 -= 1
                else:
                    return False
                change2 += 1
            else:
                if change1 > 0 and change2 > 0:
                    change1 -= 1
                    change2 -= 1
                elif change1 > 2:
                    change1 -= 3
                else:
                    return False

        return True
