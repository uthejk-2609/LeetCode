class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ""
        for i in s:
            pos = ord(i) - ord('a') + 1
            num_str += str(pos)

        for j in range(k):
            total = 0
            for digit in num_str:
                total += int(digit)
            num_str = str(total)

        return int(num_str)
