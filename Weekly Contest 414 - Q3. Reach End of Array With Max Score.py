class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        
        for i in range(n):
            for j in range(i + 1, n):
                score = (j - i)*nums[i]
                dp[j] = max(dp[j], dp[i] + score)

        return dp[-1]
