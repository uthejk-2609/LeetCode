class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        for i in range(len(nums)):
            for j in range(len(nums) - 1 -i):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        largest_num =  ''.join(nums)

        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
