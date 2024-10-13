class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(pq, int(nums[i]))
            if len(pq) > k:
                heapq.heappop(pq)

        return str(heapq.heappop(pq))
