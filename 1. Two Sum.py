class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        pair_idx = {}

        for idx, num in enumerate(nums):
            if target - num in pair_idx:
                return [idx, pair_idx[target - num]]
            pair_idx[num] = idx

"""
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
"""
