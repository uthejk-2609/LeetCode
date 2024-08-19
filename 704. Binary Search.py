class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
        
        return -1
