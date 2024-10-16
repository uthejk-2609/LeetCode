class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num, count in freq.items():
            if count > 2:
                return False

        return True
