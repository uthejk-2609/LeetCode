class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)

        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                nums[res] = nums[i+1]
                res += 1

        return res
