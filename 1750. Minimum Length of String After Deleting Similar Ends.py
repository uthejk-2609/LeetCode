class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        while i < j and s[i] == s[j]:
            curr = s[i]

            while i < len(s) and s[i] == curr:
                i = i + 1
            while j >= 0 and s[j] == curr:
                j = j - 1

            if i >= j:
                break

        return  max(j - i + 1, 0)
