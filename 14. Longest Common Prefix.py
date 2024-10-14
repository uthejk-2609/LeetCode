class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_str = max(strs)
        min_str = min(strs)
        n = len(min_str)
        res = ''

        for i in range(n):
            if min_str[i] != max_str[i]:
                return res
            res += min_str[i]

        return res
