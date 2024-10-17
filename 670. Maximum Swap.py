class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        max_idx = [-1] * n
        max_digit = '-1'
        max_pos = -1

        for i in range(n - 1, -1, -1):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_pos = i
            max_idx[i] = max_pos

        for i in range(n):
            if digits[i] < digits[max_idx[i]]:
                digits[i], digits[max_idx[i]] = digits[max_idx[i]], digits[i]
                break

        return int(''.join(digits))
