class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        res = []
        sum = 0

        for i in range(n):
            if len(res) == 0 or nums[i][0] > res[-1][1]:
                res.append(nums[i])
            else:
                res[-1][1] = max(res[-1][1], nums[i][1])

        for i in range(len(res)):
            sum += (res[i][1] - res[i][0] + 1)

        return sum

        '''
        seen = set()
        for a, b in nums:
            for i in range(a, b+1):
                seen.add(i)
        return len(seen)
        '''
