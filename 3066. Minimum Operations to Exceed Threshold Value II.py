class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and nums[0] >= k:
            return 0

        minOp = 0
        heapq.heapify(nums)

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            curr = min(x, y)*2 + max(x, y)
            heapq.heappush(nums, curr)
            minOp += 1

        return minOp
