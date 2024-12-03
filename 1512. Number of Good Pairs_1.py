class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        n = len(nums)

        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    good_pairs += 1

        return good_pairs
