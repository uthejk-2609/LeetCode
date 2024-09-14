class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_element = 0
        max_len = 0
        curr_len = 0

        for num in nums:
            max_element = max(max_element, num)

        for i in nums:
            if max_element == i:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0

        return max_len
