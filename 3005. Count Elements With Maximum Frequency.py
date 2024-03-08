class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        set_nums = set(nums)
        freq = []

        for i in set_nums:
            count = 0
            for j in nums:
                if i == j:
                    count = count + 1
            freq.append(count)

        m = max(freq)
        maxx = 0

        for i in freq:
            if m == i:
                maxx = maxx + i

        return maxx
