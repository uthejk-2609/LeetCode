class Solution:
    def minimumSteps(self, s: str) -> int:
        idx = 0
        n = len(s)
        steps = 0

        for i in range(n):
            if s[i] == '0':
                steps += (i - idx)
                idx += 1

        return steps
