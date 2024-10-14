class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        t = 1
        pq = []

        for gift in gifts:
            heapq.heappush(pq, -gift)

        while t <= k:
            curr = -heapq.heappop(pq)
            heapq.heappush(pq, -int(math.sqrt(curr)))
            t += 1

        return -(sum(pq))
