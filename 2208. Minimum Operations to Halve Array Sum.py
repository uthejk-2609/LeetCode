class Solution:
    def halveArray(self, nums: List[int]) -> int:
        pq = []
        arrSum = currSum = sum(nums)
        n = len(nums)
        min_op = 0

        for i in range(n):
            heapq.heappush(pq, -nums[i])
            
        while currSum > (arrSum / 2):
            curr = heapq.heappop(pq)
            heapq.heappush(pq, curr/2)
            currSum -= (-curr)/2
            min_op += 1

        return min_op
