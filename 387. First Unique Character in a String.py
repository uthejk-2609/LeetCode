class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq ={}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for idx, char in enumerate(s):
            if freq[char] == 1:
                return idx

        return -1
