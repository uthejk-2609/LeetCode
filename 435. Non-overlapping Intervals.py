class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        prev = intervals[0]
        count = 0

        for i in range(1, n):
            curr = intervals[i]
            if curr[0] < prev[1]:
                count += 1
                if prev[1] < curr[1]:
                    prev = prev
                else:
                    prev = curr
            else:
                prev = curr

        return count
