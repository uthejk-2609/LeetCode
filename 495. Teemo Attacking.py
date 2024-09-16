class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_duration = 0
        n = len(timeSeries)

        for i in range(1, n):
            total_duration = total_duration + min(duration, timeSeries[i] - timeSeries[i-1])

        return total_duration + duration
