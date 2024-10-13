class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for i in freq:
            if freq[i] > len(nums) // 3:
                ans.append(i)

        return ans
