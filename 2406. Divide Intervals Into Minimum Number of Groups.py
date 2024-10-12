class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res_pq = []

        for l, r in intervals:
            if not res_pq:
                heapq.heappush(res_pq, r)
            else:
                if res_pq[0] >= l:
                    heapq.heappush(res_pq, r)
                else:
                    heapq.heappop(res_pq)
                    heapq.heappush(res_pq, r)

        return len(res_pq)
