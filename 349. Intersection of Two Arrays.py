class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()

        for num in nums1:
            if num in nums2:
                seen.add(num)

        return seen
