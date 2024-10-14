class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = 0
        pq = []

        for i in range(n):
            heapq.heappush(pq, -nums[i])

        for j in range(k):
            curr = -heapq.heappop(pq)
            score += curr
            heapq.heappush(pq, -math.ceil(curr/3))
    
        return score
