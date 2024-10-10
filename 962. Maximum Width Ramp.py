class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        max_ramp = 0

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        for j in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ramp = j - stack.pop()
                max_ramp = max(max_ramp, ramp)

        return max_ramp
