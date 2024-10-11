class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        a, b = 0, 0

        while b < n:
            if nums[b] != 0:
                nums[a] = nums[b]
                a += 1
                b += 1
            else:
                b += 1

        while a < n:
            nums[a] = 0
            a += 1

        return nums
