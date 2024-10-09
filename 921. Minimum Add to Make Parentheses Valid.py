class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = 0
        close_c = 0

        for i in s:
            if i == '(':
                open_c += 1
            elif i == ')':
                if open_c > 0:
                    open_c -= 1
                else:
                    close_c += 1

        min_moves = open_c + close_c

        return min_moves
