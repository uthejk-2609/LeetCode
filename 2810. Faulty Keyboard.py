class Solution:
    def finalString(self, s: str) -> str:
        res = ""

        for j in s:
            if j != 'i':
                res += j
            else:
                res = res[::-1]

        return res
