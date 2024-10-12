class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        n = len(s)
        ans = ""

        for i in range(n):
            ans += s[i][::-1]

            if i == n-1:
                return ans

            ans += " "
