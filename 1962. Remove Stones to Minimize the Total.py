class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        n = len(piles)
        ans = 0

        for i in range(n):
            heapq.heappush(pq, -piles[i])

        for j in range(k):
            curr = -heapq.heappop(pq)
            heapq.heappush(pq, -math.ceil(curr/2))

        for i in range(n):
            ans += -pq[i]

        return ans
