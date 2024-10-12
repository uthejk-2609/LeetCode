class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i, j = 0, n - 1

        while i < j:
            if s[i] == '-' or not s[i].isalpha():
                i += 1
            if s[j] == '-' or not s[j].isalpha():
                j -= 1
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        return ''.join(s)
