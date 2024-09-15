class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        n = len(s)

        for i in range(0, n-1):
            score = score + abs(ord(s[i]) - ord(s[i+1]))

        return score
