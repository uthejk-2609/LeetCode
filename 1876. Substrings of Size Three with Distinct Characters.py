class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good = 0

        for i in range(0, len(s)-2):
            subs = s[i:i+3]
            if len(set(subs)) == len(subs):
                good += 1

        return good
