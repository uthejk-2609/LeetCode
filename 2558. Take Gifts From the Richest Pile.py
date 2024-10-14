class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        t = 1
        n = len(gifts)

        for i in range(n):
            gifts[i] *= -1
        
        heapq.heapify(gifts)

        while t <= k:
            curr = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.sqrt(curr)))
            t += 1

        return -sum(gifts)
