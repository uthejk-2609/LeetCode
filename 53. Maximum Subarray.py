class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:    return 0

        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:len(nums)]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
