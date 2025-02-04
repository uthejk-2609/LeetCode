class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        sort_arr = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sort_arr.append(left[i])
                i += 1
            else:
                sort_arr.append(right[j])
                j += 1

        while i < len(left):
            sort_arr.append(left[i])
            i += 1

        while j < len(right):
            sort_arr.append(right[j])
            j += 1

        return sort_arr
