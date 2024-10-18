class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_sq = 0

        for i in range(n):
            if n % (i + 1) == 0:
                sum_sq += nums[i] ** 2

        return sum_sq
