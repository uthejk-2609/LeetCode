class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        s = list(s)
        res = ''

        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        freq = sorted(freq.items(), key=lambda x: -x[1])

        for key, val in freq:
            res += key*val

        return res
