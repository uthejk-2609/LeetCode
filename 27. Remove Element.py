class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[j] == val:
                nums.pop()
                j = j - 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i = i + 1

        return len(nums)
