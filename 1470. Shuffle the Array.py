class Solution:
    def shuffle(nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
