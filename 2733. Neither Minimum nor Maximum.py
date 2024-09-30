class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        maxx = max(nums)
        minn = min(nums)

        for num in nums:
            if num != maxx and num != minn:
                return num
