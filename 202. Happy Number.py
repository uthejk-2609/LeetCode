class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = str(n)
        sett = set()

        while n1 not in sett:
            a = 0
            for i in n1:
                a = a + int(i)*int(i)
            sett.add(n1)
            n1 = str(a)

        return n1 == '1'
